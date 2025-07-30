from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

# 1. Создание двух пользователей
u1 = User.objects.create_user(username='user1')
u2 = User.objects.create_user(username='user2')

# 2. Создание двух авторов, связанных с пользователями
a1 = Author.objects.create(user=u1)
a2 = Author.objects.create(user=u2)

# 3. Добавление 4 категорий
cat1 = Category.objects.create(name='Спорт')
cat2 = Category.objects.create(name='Политика')
cat3 = Category.objects.create(name='Образование')
cat4 = Category.objects.create(name='Наука')

# 4. Добавление 2 статей и 1 новости
p1 = Post.objects.create(author=a1, post_type=Post.ARTICLE, title='Статья про спорт', text='Какой-то очень длинный текст про спорт...')
p2 = Post.objects.create(author=a2, post_type=Post.ARTICLE, title='Статья про политику', text='Какой-то очень длинный текст про политику...')
p3 = Post.objects.create(author=a1, post_type=Post.NEWS, title='Новость из мира науки', text='Новость, новость, новость...')

# 5. Присвоение категорий
p1.categories.add(cat1, cat4) # Статья про спорт относится к категориям "Спорт" и "Наука"
p2.categories.add(cat2)
p3.categories.add(cat4)

# 6. Создание 4 комментариев
c1 = Comment.objects.create(post=p1, user=a2.user, text='Интересная статья!')
c2 = Comment.objects.create(post=p1, user=u1, text='Спасибо за информацию.')
c3 = Comment.objects.create(post=p2, user=u2, text='Не согласен с автором.')
c4 = Comment.objects.create(post=p3, user=a1.user, text='Сам написал, сам прокомментировал.')

# 7. Применение лайков/дислайков
p1.like()
p1.like()
p2.dislike()
p3.like()
c1.like()
c4.dislike()

# 8. Обновление рейтингов пользователей
a1.update_rating()
a2.update_rating()

# 9. Вывод username и рейтинга лучшего пользователя
best_author = Author.objects.order_by('-rating').first()
print(f"Лучший автор: {best_author.user.username}, Рейтинг: {best_author.rating}")

# 10. Вывод информации о лучшей статье
best_post = Post.objects.order_by('-rating').first()
print(f"Лучшая статья:")
print(f"  Дата добавления: {best_post.created_at}")
print(f"  Автор: {best_post.author.user.username}")
print(f"  Рейтинг: {best_post.rating}")
print(f"  Заголовок: {best_post.title}")
print(f"  Превью: {best_post.preview()}")

# 11. Вывод всех комментариев к лучшей статье
print(f"\nКомментарии к статье '{best_post.title}':")
comments = Comment.objects.filter(post=best_post)
for comment in comments:
    print(f"  Дата: {comment.created_at}")
    print(f"  Пользователь: {comment.user.username}")
    print(f"  Рейтинг: {comment.rating}")
    print(f"  Текст: {comment.text}")
    print("-" * 20)
