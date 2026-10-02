// Run with Node + Playwright installed. Browser binaries must be installed separately.
const { chromium } = require('playwright');
const { pathToFileURL } = require('url');
const path = require('path');
(async()=>{
 const browser=await chromium.launch({headless:true, ...(process.env.PLAYWRIGHT_CHANNEL ? {channel:process.env.PLAYWRIGHT_CHANNEL} : {})});
 try {
 const page=await browser.newPage({viewport:{width:390,height:844}});
 await page.goto(pathToFileURL(path.join(__dirname,'prototype.html')).href);
 await page.getByRole('button',{name:'生成待确认摘要'}).click();
 if(!(await page.getByRole('alert').innerText()).includes('请填写')) throw Error('empty input was not blocked');
 await page.getByLabel('地域').fill('上海');await page.getByLabel('材料规格').fill('A规格');await page.getByLabel('数量').fill('0');
 await page.getByRole('button',{name:'生成待确认摘要'}).click();if(await page.locator('#result').isVisible())throw Error('zero quantity accepted');
 await page.getByLabel('数量').fill('10');await page.getByRole('button',{name:'生成待确认摘要'}).click();
 if(!(await page.locator('#summary').innerText()).includes('数量：10')) throw Error('summary missing');
 await page.getByRole('button',{name:'修改信息'}).click();if(!(await page.getByLabel('地域').isVisible()))throw Error('edit unavailable');
 if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('mobile overflow');
 console.log(JSON.stringify({status:'pass',tests:['missing-fields','zero-quantity','complete-summary','edit','390px-no-overflow']}));
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
