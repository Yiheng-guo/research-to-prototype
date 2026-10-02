#!/usr/bin/env python3
"""Local structured-input helper. Semantic judgments must be supplied or reviewed by a human/agent."""
import argparse, json, sys, math
from pathlib import Path
from datetime import date

def need(condition, message):
    if not condition: raise ValueError(message)
def ids(rows, label):
    seen=set()
    for row in rows:
        value=row.get('id'); need(isinstance(value,str) and value.strip(),label+' requires nonempty id')
        need(value not in seen,label+' duplicate id: '+value);seen.add(value)
    return seen
def number(value, label):
    need(not isinstance(value,bool) and isinstance(value,(int,float)) and math.isfinite(value),label+' must be finite number');return value

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path); parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    try:
        need(not args.output.exists(),'refusing to overwrite output')
        data=json.loads(args.input.read_text(encoding='utf-8'));need(isinstance(data,dict),'input must be object')
        result=process(data)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf-8') as f: json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
        print(json.dumps({'output':str(args.output),'status':result.get('status','completed')},ensure_ascii=False))
        return 0 if result.get('status') not in ('blocked','failed') else 2
    except (ValueError,KeyError,TypeError,OSError) as e: print('error: '+str(e),file=sys.stderr);return 2

def process(d):
    evidence={r['id']:r for r in d['evidence']};ids(d['evidence'],'evidence');requirements=d['requirements'];need(requirements,'requirements required');ids(requirements,'requirements');gaps=[]
    for r in requirements:
        need(r.get('evidence_ids'),'requirement evidence required');need(set(r['evidence_ids'])<=set(evidence),'unknown evidence id')
        need(r.get('acceptance') and r.get('flow') and r.get('validation_method'),'flow/acceptance/validation required')
        if all(evidence[x]['kind']!='fact' for x in r['evidence_ids']):gaps.append({'requirement':r['id'],'issue':'hypothesis only; experiment before commitment'})
    return {'status':'prototype_brief_ready','version':d['version'],'requirements':requirements,'gaps':gaps,'changes':d.get('changes',[]),'acceptance_matrix':[{'requirement':r['id'],'steps':r['flow'],'expected':r['acceptance'],'method':r['validation_method']} for r in requirements],'limits':'Traceability is checked; usability, demand and production feasibility require separate tests.'}

if __name__ == "__main__": raise SystemExit(main())
