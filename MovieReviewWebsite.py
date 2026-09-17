"""A small local movie-review website using only Python's standard library.

Run this file and open http://localhost:8000 in a browser.
"""

from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

REVIEWS = [
    {"movie": "Interstellar", "rating": "5", "review": "A beautiful space adventure."},
    {"movie": "The Lion King", "rating": "4", "review": "A timeless family film."},
]


def page() -> str:
    cards = "".join(
        f"<article><h3>{escape(item['movie'])} <span>{escape(item['rating'])}/5</span></h3>"
        f"<p>{escape(item['review'])}</p></article>"
        for item in reversed(REVIEWS)
    )
    return f"""<!doctype html><html><head><title>Movie Reviews</title>
    <style>body{{font:16px Arial;max-width:720px;margin:40px auto;background:#f5f7fb}}
    article,form{{background:white;padding:18px;margin:14px 0;border-radius:10px;box-shadow:0 2px 8px #ccd}}
    input,textarea,button{{display:block;width:96%;padding:9px;margin:8px 0}}span{{color:#b36b00}}</style>
    </head><body><h1>Movie Review Hub</h1>{cards}
    <form method='post'><h2>Write a review</h2><input required name='movie' placeholder='Movie title'>
    <input required type='number' name='rating' min='1' max='5' placeholder='Rating (1-5)'>
    <textarea required name='review' placeholder='Your review'></textarea><button>Publish review</button></form>
    </body></html>"""


class ReviewHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        body = page().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:
        size = int(self.headers.get("Content-Length", "0"))
        form = parse_qs(self.rfile.read(size).decode())
        movie, rating, review = (form.get(name, [""])[0].strip() for name in ("movie", "rating", "review"))
        if movie and rating in {"1", "2", "3", "4", "5"} and review:
            REVIEWS.append({"movie": movie, "rating": rating, "review": review})
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        return


if __name__ == "__main__":
    print("Movie Review Hub running at http://localhost:8000 (Ctrl+C to stop)")
    HTTPServer(("localhost", 8000), ReviewHandler).serve_forever()
