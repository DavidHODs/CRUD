from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A simple title'),
        self.assertEqual(str(post), Post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_views(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def entry_create(request):
        form = BlogEntryForm()
        if request.method == "POST":
            form = BlogEntryForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect(reverse('entries'))
                form.save()
        return render(request, "blog/entry_create.html", {'form': form})

    def test_invalid_entry_create(self):
        self.c.login(username='test', password='test')
        data = {'text': 'Test text'}
        response = self.c.post(reverse('entry_create'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "title",
                             "This field is required.")

    def test_valid_entry_create(self):
        self.c.login(username='test', password='test')
        data = {'text': 'Test text', 'title': 'Test title'}
        data['user'] = self.user.id
        self.assertEqual(BlogEntry.objects.count(), 0)
        response = self.c.post(reverse('entry_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogEntry.objects.count(), 1)

    def test_entry_custom_managers(self):
        BlogEntry.objects.create(
            title='Test', text='Test', user=self.user, is_published=False)
        BlogEntry.objects.create(title='Test', text='Test', user=self.user)
        self.assertEqual(BlogEntry.objects.count(), 2)
        self.assertEqual(BlogEntry.published.count(), 1)

    def test_entries_template_context(self):
        BlogEntry.objects.create(title='Test', text='Test', user=self.user)
        BlogEntry.objects.create(title='Test', text='Test', user=self.user)
        BlogEntry.objects.create(
            title='Test', text='Test', user=self.user, is_published=False)

        response = self.c.get(reverse('entries'))
        self.assertEqual(len(response.context['entries']), 2)

    def entries_page(request, page):
        page = int(page)
        entries = BlogEntry.published.all()
        paginator = Paginator(entries, 10)  # 10 entries per page
        if page > paginator.num_pages:
            raise Http404()
        page_ = paginator.page(page)
        object_list = page_.object_list
        return render(request, "blog/entries_page.html", {"entries": object_list})
