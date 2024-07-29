from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def gen_resume(request):
    if request.method == 'POST':
        context = {
            'name': request.POST.get('name', ''),
            'about': request.POST.get('about', ''),
            'age': request.POST.get('age', ''),
            'email': request.POST.get('email', ''),
            'phone': request.POST.get('phone', ''),
            'skills': [request.POST.get(f'skill{i}', '') for i in range(1, 6)],
            'education': [
                {
                    'degree': request.POST.get(f'degree{i}', ''),
                    'college': request.POST.get(f'college{i}', ''),
                    'year': request.POST.get(f'year{i}', '')
                } for i in range(1, 4)
            ],
            'languages': [request.POST.get(f'lang{i}', '') for i in range(1, 4)],
            'projects': [
                {
                    'title': request.POST.get(f'project{i}', ''),
                    'duration': request.POST.get(f'duration{i}', ''),
                    'description': request.POST.get(f'desc{i}', '')
                } for i in range(1, 3)
            ],
            'experience': [
                {
                    'company': request.POST.get(f'company{i}', ''),
                    'post': request.POST.get(f'post{i}', ''),
                    'duration': request.POST.get(f'duration{i}', ''),
                    'description': request.POST.get(f'lin{i}1', '')
                } for i in range(1, 3)
            ],
            'achievements': [request.POST.get(f'ach{i}', '') for i in range(1, 4)],
        }
        return render(request, 'resume.html', context)
    return render(request, 'index.html')
