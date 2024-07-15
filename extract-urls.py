import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_urls(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, 'xml')
    urls = [element.text for element in soup.find_all('loc')]
    return urls

def write_urls_to_file(urls, filename):
    with open(filename, 'w') as f:
        for url in urls:
            f.write(url + '\n')

def is_page_url(url):
    # Define patterns for URLs that are not pages
    non_page_patterns = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.xml', '.css', '.js']
    return not any(pattern in url for pattern in non_page_patterns)

def process_sitemap(sitemap_url):
    urls = extract_urls(sitemap_url)
    all_urls = []
    for url in urls:
        if 'sitemap' in url:
            all_urls.extend(process_sitemap(url))
        else:
            if is_page_url(url):
                all_urls.append(url)
    return all_urls

def start_extraction():
    sitemap_url = entry_url.get()
    output_file = entry_file.get()

    if not sitemap_url or not output_file:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        all_urls = process_sitemap(sitemap_url)
        write_urls_to_file(all_urls, output_file)
        messagebox.showinfo("Success", "URLs extracted and saved to {}".format(output_file))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Sitemap URL Extractor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_url = tk.Label(frame, text="Sitemap URL:")
label_url.grid(row=0, column=0, sticky=tk.W, pady=2)

entry_url = tk.Entry(frame, width=50)
entry_url.grid(row=0, column=1, pady=2)

label_file = tk.Label(frame, text="Output File:")
label_file.grid(row=1, column=0, sticky=tk.W, pady=2)

entry_file = tk.Entry(frame, width=50)
entry_file.grid(row=1, column=1, pady=2)

browse_button = tk.Button(frame, text="Browse", command=lambda: entry_file.insert(0, filedialog.asksaveasfilename()))
browse_button.grid(row=1, column=2, pady=2)

start_button = tk.Button(frame, text="Start Extraction", command=start_extraction)
start_button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
