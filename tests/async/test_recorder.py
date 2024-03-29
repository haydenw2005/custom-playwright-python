import pytest
from playwright.async_api import async_playwright
import asyncio

@pytest.mark.asyncio
async def test_enable_recorder():
    async with async_playwright() as p:
        # Launch the browser in non-headless mode
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
    
            
        )
        page = await context.new_page()
        await page.goto("https://playwright.dev/python/docs/intro")
        # Enable the recorder
        await context.enable_recorder(language='jsonl', mode='recording', output_file='outputsignup.jsonl')
        # Use asyncio.sleep instead of time.sleep for asynchronous sleep
        await asyncio.sleep(5)
        # Add assertions or further actions to validate recorder functionality
        await browser.close()