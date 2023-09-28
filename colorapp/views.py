from django.shortcuts import render
from PIL import Image
from collections import Counter



def extract_colors(request):
    if request.method == 'POST':
        image = request.FILES['image']
        with Image.open(image) as img:
            img = img.resize((200, 200))  # Resize for faster processing
            avg_color = img.convert("RGB").getpixel((100, 100))  # Get the average color of the center pixel
            main_color = f'rgb({avg_color[0]}, {avg_color[1]}, {avg_color[2]})'
        
        def rgb_to_hex(rgb):
          return '#%02x%02x%02x' % rgb
        
        text_value = request.POST.get('text_value', rgb_to_hex(avg_color))
        return render(request, 'index.html', {'main_color': main_color, 'text_value':text_value})
    
    return render(request, 'index.html')


