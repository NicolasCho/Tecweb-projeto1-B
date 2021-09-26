from django.shortcuts import render, redirect
from .models import Note
from .models import Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_request = request.POST.get('tag-input')
        tag_db = Tag(tag_str = tag_request)

        #https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.exists
        if not Tag.objects.filter(pk=tag_request).exists():
           tag_db.save()
    
        

        nota = Note(title=title, content=content, tag=tag_db)
        nota.save()
        
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('deletar')
        note = Note.objects.filter(id=id).first()#.delete()
        deleted_note_tag = note.tag
        note.delete()

        #Deleta tag do db se náo existir mais notas com essa tag
        if not Note.objects.filter(tag=deleted_note_tag.tag_str).exists():
            deleted_note_tag.delete()

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update(request):
    if request.method == 'POST':
        new_title = request.POST.get('titulo')
        new_content = request.POST.get('detalhes')
        id = request.POST.get('id')

        new_tag = request.POST.get('edit-tag-input')
        tag_db = Tag(tag_str = new_tag)
        if not Tag.objects.filter(pk=new_tag).exists():
            tag_db.save()

        note = Note.objects.filter(id=id)
        old_tag = note.first().tag
        note.update(title = new_title, content = new_content, tag=tag_db)

        #Ao atualizar, se náo existirem mais notas com a tag antiga, deletar tag do db
        if not Note.objects.filter(tag=old_tag.tag_str).exists():
            old_tag.delete()

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def taglist(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/taglist.html', {'tags': all_tags})

def tags(request, tag_str):
    tag = Tag.objects.filter(tag_str=tag_str).first()
    tag_notes = Note.objects.filter(tag = tag_str)
    return render(request, 'notes/tags.html', {'notes':tag_notes,'tag':tag})
