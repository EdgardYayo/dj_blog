from django.shortcuts import render

from datetime import date

all_posts = [
    {
        "slug": "snake",
        "image": "python-cartoon-2.jpg",
        "author": "Severus Snape",
        "date": date(2022, 10, 31),
        "title": "Learn Parsel with me",
        "excerpt": "Unlock the Secrets of Parseltongue: Enroll in the Exclusive Serpentine Language Course",
        "content": "Do you hear the faint hissing whispers that seem to beckon you from the shadows? Have you always felt a deep, inexplicable connection to the serpentine realm? If so, you may possess the rare and extraordinary gift of Parseltongue – the ancient language of snakes.",
    },
    {
        "slug": "potter-blog",
        "image": "python-cartoon.png",
        "author": "Harry Potter",
        "date": date(2023, 11, 25),
        "title": "How am I defeated Voldemort",
        "excerpt": "As I stand here today, I can vividly recall the moments leading up to that fateful night when I faced Voldemort for the last time. ",
        "content": "In the Great Hall of Hogwarts, I faced Voldemort for the final battle, our wands locked in a brilliant display of priori incantatem. Drawing upon the love of my friends and family, I channeled a force more powerful than his dark magic. My righteous fury engulfed Voldemort's Killing Curse, ending his reign of terror as his wand clattered to the ground. It was a victory for all who fought against evil, a triumph of hope over despair and light over darkness.",
    },
    {
        "slug": "hermione-blog",
        "image": "python-cartoon.png",
        "author": "Hermione Granger",
        "date": date(2023, 10, 15),
        "title": "The Power of Knowledge",
        "excerpt": "From the moment I stepped into the wizarding world, I was captivated by the vast expanse of knowledge that lay before me.",
        "content": "Knowledge has been my constant companion, a guiding light that has illuminated my path through even the darkest of times. Whether it was mastering complex spells, unraveling ancient runes, or delving into the intricate laws that govern our magical society, the pursuit of understanding has been my unwavering passion. True power lies not in the might of a wand, but in the depths of one's intellect and the ability to wield knowledge as a formidable weapon against ignorance and oppression. It was this conviction that drove me to seek out answers, to challenge conventions, and to fight for a world where wisdom prevails over prejudice.",
    },
    {
        "slug": "dumbledore-blog",
        "image": "python-cartoon.png",
        "author": "Albus Dumbledore",
        "date": date(2023, 12, 1),
        "title": "Love's Eternal Radiance",
        "excerpt": "In a world often shrouded in darkness, it is love that serves as the guiding beacon, illuminating the path towards hope and redemption.",
        "content": "Throughout my long journey, I have witnessed the profound power of love to transcend boundaries, heal wounds, and vanquish even the deepest shadows. It is a force that knows no limits, capable of turning foes into allies and transforming the most hardened hearts. Love's radiance shines brightest in the face of adversity, for it is in those moments that its true strength is revealed. Whether it manifests as the unwavering bond between friends, the selfless sacrifice of a parent, or the courage to forgive one's enemies, love is the ultimate expression of our humanity. It is the beacon that guides us through the darkest of nights, reminding us that even in the bleakest of circumstances, there is always the potential for redemption and a brighter tomorrow.",
    },
]

def get_date(post):
    return post.get("date")

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": post
    })
