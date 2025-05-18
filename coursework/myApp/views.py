from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ContactForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def about(request):
    reviews = [
        {'author': 'Екатерина Смирнова, маркетолог в ИТ-компании', 'text': 'Сотрудничаем с SUVE.PRO уже не первый год. Заказываем как корпоративные сувениры, так и оформление мероприятий под ключ. Особенно радует, что компания всегда предлагает свежие идеи и нестандартные решения. Последний заказ был выполнен раньше срока, и качество, как всегда, на высоте. Команда очень отзывчивая и всегда на связи.'},
        {'author': 'Александр Павлов, руководитель отдела закупок', 'text': 'Мы обратились в SUVE.PRO с нестандартной задачей: брендировать сувениры к корпоративному мероприятию для 300+ сотрудников. Была разработана уникальная концепция, предложены несколько вариантов дизайна и подобран качественный мерч. Всё было доставлено вовремя и без задержек. Отдельное спасибо за внимательное отношение к мелочам!'},
        {'author': 'Ольга Чернова, специалист по PR', 'text': 'Очень довольна уровнем сервиса. Заказывали подарки для партнёров — ежедневники, термокружки, брендированные ручки. Отдельно хочу отметить качество упаковки и нанесения логотипа — всё выглядит дорого и стильно. Менеджеры оперативно реагировали на правки и предоставили все макеты в срок. Рекомендую!'},
        {'author': 'Игорь Власов, директор агентства событийного маркетинга', 'text': 'Нам важно, чтобы партнёры были надёжными и точными в сроках. SUVE.PRO — именно такие. Несколько раз спасали нас в условиях сжатых дедлайнов, при этом продукция всегда высокого качества. Один из немногих подрядчиков, кому действительно можно доверять. Всегда приятно работать с профессионалами.'},
        {'author': 'Алина Захарова, HR-менеджер', 'text': 'Понадобилось срочно подготовить приветственные наборы для новых сотрудников. SUVE.PRO подобрали стильные решения, оформили всё с фирменным стилем и доставили уже через 3 дня. Новый сотрудник получил коробку, и у него был вау-эффект — всё выглядело как подарок, а не просто канцелярия. Спасибо!'},
        {'author': 'Максим Беляев, предприниматель', 'text': 'Сравнивал несколько компаний по нанесению логотипов на продукцию — остановился на SUVE.PRO и не пожалел. Отличная коммуникация, возможность быстро согласовать макеты и внести изменения, а главное — результат превзошёл ожидания. Заказывал брендированные футболки, блокноты и флешки — всё было выполнено на высшем уровне.'},
    ]
    return render(request, 'about.html', {'reviews': reviews})

def catalog(request):
    categories = Category.objects.all()
    return render(request, 'catalog.html', {'categories': categories})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })

def portfolio(request):
    return render(request, 'portfolio.html')

def production(request):
    return render(request, 'production.html')

def payment_delivery(request):
    return render(request, 'payment_delivery.html')

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше обращение успешно отправлено!')
            return redirect('contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})

def project_umschool(request):
    return render(request, 'project_umschool.html')

def project_digitalskills(request):
    return render(request, 'project_digitalskills.html')

def project_fifa(request):
    return render(request, 'project_fifa.html')

def project_sport(request):
    return render(request, 'project_sport.html')

def project_tatmedia(request):
    return render(request, 'project_tatmedia.html')

def project_volunteer(request):
    return render(request, 'project_volunteer.html')

