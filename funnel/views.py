from django.shortcuts import render, redirect
from .models import Lead

def quiz_view(request, step=1):
    questions = {
        1: {
            "text": "What is your #1 body goal?",
            "options": {"A": "Lose belly fat & bloat", "B": "Drop overall weight", "C": "Tone up & build muscle"}
        },
        2: {
            "text": "When do sugar cravings hit hardest?",
            "options": {"A": "Morning", "B": "3:00 PM slump", "C": "Late at night"}
        },
        3: {
            "text": "How do you feel when you wake up?",
            "options": {"A": "Energized", "B": "Completely exhausted", "C": "I wake up at night"}
        },
        4: {
            "text": "Does the scale stay stuck even when you diet?",
            "options": {"A": "Yes, it's so frustrating!", "B": "Sometimes.", "C": "No."}
        },
        5: {
            "text": "How much daily time do you have for a routine?",
            "options": {"A": "Barely 10 minutes", "B": "30 minutes", "C": "1 hour+"}
        },
        6: {
            "text": "Ready to see your custom action plan?",
            "options": {"A": "Yes, show me!", "B": "I'm just curious."}
        }
    }

    if request.method == 'POST':
        answer = request.POST.get('answer')
        request.session[f'question_{step}'] = answer
        
        if step < 6:
            return redirect('quiz_step', step=step+1)
        else:
            # 6. soru bittiğinde Köprü Sayfasına fırlatır!
            return redirect('bridge_page')

    context = {
        'step': step,
        'question': questions[step]
    }
    return render(request, 'funnel/quiz.html', context)


# --- views.py içindeki bridge_page fonksiyonu ---

def bridge_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        q1_answer = request.session.get('question_1', 'A') 
        
        # SİSTEMİ BURADA ZEKİLEŞTİRİYORUZ
        # Eğer bu e-posta varsa bul ve hedefini/telefonunu güncelle, yoksa sıfırdan yarat!
        yeni_lead, created = Lead.objects.update_or_create(
            email=email,
            defaults={
                'phone_number': phone,
                'primary_goal': q1_answer
            }
        )
        
        if phone:
            import requests
            try:
                requests.post("https://api.cpanetwork.com/track", data={"offer_id": "5566", "phone": phone, "sub_id": yeni_lead.sub_id}, timeout=2)
            except:
                pass 
        
        return redirect('dashboard') 

    return render(request, 'funnel/bridge.html')


# --- YENİ EKLENEN PANO (DASHBOARD) FONKSİYONU ---
def dashboard_view(request):
    # Kullanıcının hedefini hafızadan çekiyoruz (A, B veya C)
    goal = request.session.get('question_1', 'A')
    
    # Bu hedefi HTML tasarımına gönderiyoruz ki ürünleri ona göre dizsin
    context = {'goal': goal}
    return render(request, 'funnel/dashboard.html', context)
def blank_page(request, page_name):
    # Hangi linke tıklandığını isminden anlar (örn: "shop")
    return render(request, 'funnel/blank.html', {'page_name': page_name.upper()})
def landing_page(request):
    # Ana kapıdan girenleri artık yepyeni Landing Page'e alıyoruz
    return render(request, 'funnel/landing.html')
from django.shortcuts import render

def quiz_view(request):
    # Eğer kullanıcı formu doldurup gönderirse (POST) API işlemleri buraya gelecek.
    # Şimdilik sadece HTML sayfasını ekrana basıyoruz (GET).
    return render(request, 'funnel/index.html')
def save_goal(request):
    # JS'den gelen hedefi oturuma (session) kaydeder
    goal = request.GET.get('goal', 'A')
    request.session['question_1'] = goal
    from django.http import JsonResponse
    return JsonResponse({'status': 'ok'})

# bridge_page ve dashboard_view fonksiyonların olduğu gibi kalsın...