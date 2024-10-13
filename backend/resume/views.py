from django.shortcuts import render, redirect
from .models import Resume


# Create your views here.
def index(request):
    if request.method == "POST":
        resume = Resume(
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            education=request.POST["education"],
            experience=request.POST["experience"],
            skills=request.POST["skills"],
        )
        resume.save()
        return redirect("preview", pk=resume.pk)

    return render(request, "resume/index.html")  # 渲染表单页面


def preview(request, pk):
    resume = Resume.objects.get(pk=pk)
    return render(request, "resume/preview.html", {"resume": resume})
