import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def scrape_audio(url):
    response = requests.get(url)  # Send a GET request to the URL
    audio_filename = 'scraped_audio.mp3'
    with open(audio_filename, 'wb') as file:  # Save the audio content to a file
        file.write(response.content)
    print("Audio data has been scraped and saved to scraped_audio.mp3")
    
    # Save audio data to CSV
    with open('scraped_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Audio', audio_filename, url])

def scrape_image(url):
    response = requests.get(url)  # Send a GET request to the URL
    image_filename = 'scraped_image.jpg'
    with open(image_filename, 'wb') as file:  # Save the image content to a file
        file.write(response.content)
    print("Image data has been scraped and saved to scraped_image.jpg")
    
    # Save image data to CSV
    with open('scraped_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Image', image_filename, url])

def scrape_pdf(url):
    response = requests.get(url)  # Send a GET request to the URL
    pdf_filename = 'scraped_document.pdf'
    with open(pdf_filename, 'wb') as file:  # Save the PDF content to a file
        file.write(response.content)
    print("PDF data has been scraped and saved to scraped_document.pdf")
    
    # Save PDF data to CSV
    with open('scraped_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['PDF', pdf_filename, url])

def main():
    url = input("Enter the URL to scrape: ")
    data_type = input("Enter the type of data to scrape (text, audio, image, pdf, html): ").lower()

    if data_type == 'text':
        scrape_text(url)
    elif data_type == 'audio':
        scrape_audio(url)
    elif data_type == 'image':
        scrape_image(url)
    elif data_type == 'pdf':
        scrape_pdf(url)
    elif data_type == 'html':
        scrape_html(url)
    else:
        print("Unsupported data type. Please choose from text, audio, image, pdf, or html.")

if __name__ == "__main__":
    main()