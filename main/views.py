from django.shortcuts import render

def home(request):
    return render(request, "main/home.html")

def menu(request):
    items = [
        {"name": "Pizza", "price": "₹199", "image": "https://upload.wikimedia.org/wikipedia/commons/9/91/Pizza-3007395.jpg"},

        {"name": "Burger", "price": "₹199", "image": "https://images.unsplash.com/photo-1550547660-d9450f859349"},

        {"name": "pasta", "price": "₹129", "image": "https://tiffinandteaofficial.com/wp-content/uploads/2021/01/IMG_3812-1-scaled-e1670948948885.jpg"},

        {"name": "Chapati roll", "price": "₹199", "image": "https://recipesblob.oetker.in/assets/b777acee3b1b47299ae7f47715e926fd/1272x764/roti-roll.webp"},

        {"name": "sandwich", "price": "₹399", "image": "https://static.toiimg.com/thumb/83740315.cms?imgsize=361903&width=800&height=800"},

        {"name": "french fries", "price": "₹299", "image": "https://www.awesomecuisine.com/wp-content/uploads/2009/05/french-fries.jpg"},

        {"name": "noodles", "price": "₹129", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOtHkeg3ozBJdDw_AxSa-F_y7X1UDMc8VjKw&s"},

        {"name": "manchurian", "price": "₹329", "image": "https://holycowvegan.net/wp-content/uploads/2020/03/veg-manchurian-7.jpg"},

       {"name": "Fried Rice", "price": "₹240", "image": "https://shwetainthekitchen.com/wp-content/uploads/2023/06/veg-fried-rice.jpg"},

       {"name": "Chicken biryani", "price": "₹123", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwaF6-1Auf1DuOXo9FhalxTrx1j-BnkoOu4A&s"},

        {"name": "Veg Biryani", "price": "₹99", "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2019/04/veg-biryani-recipe-500x500.jpg"},

        {"name": "Grilled Chicken", "price": "₹123", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwCumlA0dSUlr-yiysYOYV4xCsf3YkKY5whQ&s"},

        {"name": "Momos", "price": "₹99", "image": "https://static.toiimg.com/thumb/60275824.cms?imgsize=1041917&width=800&height=800"},

        {"name": "Icecream", "price": "₹69", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckl7ltXaMqyN2oVF74NXUwsiLxRuzIHh4Hg&s"},

        {"name": "Milkshake", "price": "₹69", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlB3xfo8yZVAiN8vRO3erAMaj6jrpnk5685A&s"},

    ]
    return render(request, "main/menu.html", {"items": items})


def contact(request):
    return render(request, "main/contact.html")
