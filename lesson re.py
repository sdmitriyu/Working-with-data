import re


def extract_image_links(html_text):
    image_links = re.findall(r'<img[^>]*src=[\'"]([^\'"]+)[\'"]', html_text)
    filtered_links = [link for link in image_links if link.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return filtered_links


sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"
image_links = extract_image_links(sample_html)

if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")
