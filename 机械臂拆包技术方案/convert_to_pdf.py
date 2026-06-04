import os
from playwright.sync_api import sync_playwright

work_dir = r'c:\Users\WZH\Desktop\documents\1'
html_path = os.path.join(work_dir, '机械臂拆包技术方案.html')
pdf_path = os.path.join(work_dir, '机械臂拆包技术方案.pdf')

print(f'Source HTML: {html_path}')
print(f'Exists: {os.path.exists(html_path)}')

# Use file:// URL with proper encoding
file_url = 'file:///' + html_path.replace('\\', '/')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    print(f'Loading: {file_url}')
    page.goto(file_url, wait_until='networkidle', timeout=30000)

    # Wait for JS to execute (TOC generation)
    page.wait_for_timeout(2000)

    # Get page title to verify
    title = page.title()
    print(f'Page title: {title}')

    # Generate PDF with proper settings
    page.pdf(
        path=pdf_path,
        format='A4',
        print_background=True,
        margin={
            'top': '15mm',
            'bottom': '15mm',
            'left': '12mm',
            'right': '12mm'
        },
        display_header_footer=False,
        prefer_css_page_size=True,
    )

    browser.close()

size_kb = os.path.getsize(pdf_path) / 1024
print(f'PDF size: {size_kb:.0f} KB')

# Verify
from pypdf import PdfReader
reader = PdfReader(pdf_path)
print(f'Pages: {len(reader.pages)}')
text = reader.pages[0].extract_text()
print(f'Page 1 preview: {text[:200]}')
print()
print('✅ PDF generation SUCCESS!')
