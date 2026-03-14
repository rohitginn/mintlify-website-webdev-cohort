import re

content = open('C:/Users/Rohit/AppData/Local/Temp/mintlify.html', 'r', encoding='utf-8').read()

assistant_match = re.search(r'<div class="rounded-[^"]*border[^>]*><div class="[^>]*><p [^>]*>Assistant</p><h4[^>]*>Intelligent assistance for your users</h4>.*?</p></div>.*?</div>', content)
if not assistant_match:
    assistant_match = re.search(r'(<div[^>]*>.*?Assistant.*?Intelligent assistance for your users.*?)<section', content)

enterprise_match = re.search(r'<section class="bg-background-soft[^>]*>.*?</section>', content)

unlock_match = re.search(r'<section class="relative w-full max-w-5xl mx-auto overflow-hidden[^>]*>.*?</section>', content)
if not unlock_match:
    unlock_match = re.search(r'(<section[^>]*>.*?Unlock knowledge for any industry.*?</section>)', content)

cta_match = re.search(r'<section class="relative mx-auto w-full md:px-8 px-6 pt-32 pb-48[^>]*>.*?</section>', content)
if not cta_match:
    cta_match = re.search(r'(<section[^>]*>.*?Make documentation your winning advantage.*?</section>)', content)

footer_match = re.search(r'<footer.*?</footer>', content)

with open('C:/Users/Rohit/AppData/Local/Temp/mintlify_extracted.html', 'w', encoding='utf-8') as f:
    f.write('<!-- ASSISTANT -->\n')
    if assistant_match:
        f.write(assistant_match.group(1) if assistant_match.lastindex else assistant_match.group(0) + '\n\n')
    f.write('\n\n<!-- ENTERPRISE -->\n')
    if enterprise_match:
        f.write(enterprise_match.group(0) + '\n\n')
    f.write('<!-- UNLOCK -->\n')
    if unlock_match:
        f.write(unlock_match.group(0) + '\n\n')
    f.write('<!-- CTA -->\n')
    if cta_match:
        f.write(cta_match.group(0) + '\n\n')
    f.write('<!-- FOOTER -->\n')
    if footer_match:
        f.write(footer_match.group(0) + '\n\n')
