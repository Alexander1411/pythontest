from flask import Flask
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!") #indent this line
if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080') # indent this line

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=ABeeZee:ital@0;1&family=Girassol&family=Josefin+Slab:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Mulish:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Noto+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;1,100;1,300;1,400;1,500;1,700&display=swap"
      rel="stylesheet"
    />

    <script
      defer
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
      crossorigin="anonymous"
    ></script>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
    />
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
    />

    <title>DBS Ecommerce</title>
  </head>
  <body>
    <!-- Sub-Navbar -->
    <nav class="navbar bg-body-tertiary">
      <div class="container">
        <div class="nav-links">
          <ul class="nav">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="womencatalog.html"
                >women</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="mancatalog.html">men</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="salescatalog.html">sales</a>
            </li>
          </ul>
        </div>
        <div class="icon-nav-conteiner">
          <a class="navbar-brand" href="index.html">
            <i class="bi bi-person icon-nav"></i>
          </a>
          <a class="navbar-brand" href="#">
            <i class="bi bi-heart icon-nav"></i>
            <a class="navbar-brand" href="#">
              <i class="bi bi-bag icon-nav"></i>
            </a>
          </a>
        </div>
      </div>
    </nav>
    <!-- End of Sub-Navbar -->
    <div class="container-default">
      <!-- Navbar -->
      <div class="open-navbar-icon-main navbar-icon-main center">
        <div class="line-main"></div>
        <div class="line-main"></div>
        <div class="line-main"></div>
      </div>
      <div class="navbar-wrapper-main">
        <nav class="navbar-main">
          <div class="close-navbar-icon-main navbar-icon-main center">
            <div class="line-main line-1"></div>
            <div class="line-main line-2"></div>
          </div>
          <div class="nav-list-main">
            <a href="index.html" class="nav-link-main center">Home</a>
            <a href="register.html" class="nav-link-main center">Login</a>
            <a href="#testimonial-section" class="nav-link-main center"
              >About Us</a
            >
            <a href="register.html" class="nav-link-main center">Register</a>
            <a href="girlscatalogo.html" class="nav-link-main center">Orders</a>
          </div>
        </nav>
      </div>

      <!-- Header -->
      <header class="header">
        <div class="center">
          <!-- Search Input -->
          <div class="search-input-wrapper">
            <div class="search-input">
              <input type="text" placeholder="Search" />
              <i class="fas fa-times"></i>
            </div>
          </div>
          <div class="search-icon">
            <i class="fas fa-search"></i>
          </div>
        </div>
        <!-- End of Search Input -->
        <div class="center">
          <div class="header-text">
            <h1 class="heading">Outdoor life</h1>
            <p class="header-paragraph">
              It’s okay to live a life others don’t understand
            </p>
          </div>
          <img
            src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/Man/hero-img.png"
            alt="Header Image"
            class="header-img"
          />
          <div class="logo">
            <h1>
              <span class="center">G</span>
              <span class="center">Y</span>
              <span class="center">M</span>
              <span class="center">B</span>
              <span class="center">S</span>
            </h1>
          </div>
        </div>
      </header>
      <!-- End of Header -->

      <!--Section catalog slides-->
      <section class="section-slides">
        <div class="slideshow-wrapper">
          <div class="slides-card">
            <div class="slides">
              <div class="slide slide-1">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/Man/man01.png"
                  alt="Man wearing gym cloths"
                  class="card-img"
                />
              </div>
              <div class="slide slide-2">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/Man/man02.png"
                  alt="Man wearing gym cloths"
                  class="card-img"
                />
              </div>
              <div class="slide slide-3">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/Man/man03.png"
                  alt="Man wearing gym cloths"
                  class="card-img"
                />
              </div>
              <div class="description-section">
                <h1 class="title-clothes">Mens</h1>
                <button
                  class="navigation-btn"
                  onclick="btnCatalog()"
                  id="btn-men-catalog"
                >
                  More &gt;&gt;
                </button>
              </div>
            </div>
          </div>
          <div class="slides-card">
            <div class="slides">
              <div class="slide-01 slide-1">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/woman/woman01.png"
                  alt="Woman wearing gym cloths"
                  class="card-img"
                />
              </div>
              <div class="slide-01 slide-2">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/woman/woman02.png"
                  alt="Woman wearing gym cloths"
                  class="card-img"
                />
              </div>
              <div class="slide-01 slide-3">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/woman/woman04.png"
                  alt="Woman wearing gym cloths"
                  class="card-img"
                />
              </div>
              <h1 class="title-clothes">Women</h1>
              <button
                class="navigation-btn"
                onclick="btnCatalog()"
                id="btn-women-catalog"
              >
                More &gt;&gt;
              </button>
            </div>
          </div>
          <div class="slides-card">
            <div class="slides">
              <div class="slide-02 slide-1">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/Man/man06.png"
                  alt=""
                  class="card-img"
                />
              </div>
              <div class="slide-02 slide-2">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/Man/man07.png"
                  alt=""
                  class="card-img"
                />
              </div>
              <div class="slide-02 slide-3">
                <img
                  src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/woman/woman08.png"
                  alt="Woman wearing gym cloths"
                  class="card-img"
                />
              </div>
              <h1 class="title-clothes">Sales</h1>
              <button
                class="navigation-btn"
                onclick="btnCatalog()"
                id="btn-sales-catalog"
              >
                More &gt;&gt;
              </button>
            </div>
          </div>
        </div>
      </section>
      <!-- End of Slides images -->

      <!-- Testimonial section -->
      <section class="testimonial" id="testimonial-section">
        <div class="video-container">
          <video class="bg-video" autoplay muted loop>
            <source
              src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/Videos/testimonial-section-video.mp4"
              type="video/mp4"
            />
          </video>
        </div>
        <div class="testimonial-wrapper">
          <div class="testimonial-bg">
            <div class="story">
              <img
                src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/Man/testimonial-01.jpg"
                alt=""
                class="story-img"
              />
              <div class="story-text">
                <h1 class="story-heading">
                  The antidote to exhaustion isn’t rest. It’s nature.
                </h1>
                <p class="story-paragraph">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus
                  accusantium officiis magni architecto aspernatur odio et
                  voluptatum perspiciatis qui necessitatibus vero aut, iste, ut
                  impedit velit mollitia laudantium asperiores voluptates!
                </p>
              </div>
            </div>
          </div>
          <div class="testimonial-bg">
            <div class="story">
              <img
                src="https://dbsecommerce.s3.eu-west-1.amazonaws.com/images/woman/testimonial-girls.jpg"
                alt=""
                class="story-img"
              />
              <div class="story-text">
                <h1 class="story-heading">
                  In all things of nature there is something of the marvellous.
                </h1>
                <p class="story-paragraph">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus
                  accusantium officiis magni architecto aspernatur odio et
                  voluptatum perspiciatis qui necessitatibus vero aut, iste, ut
                  impedit velit mollitia laudantium asperiores voluptates!
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!--End of Testimonials-->

      <!-- Footer -->
      <footer class="footer">
        <div class="footer-list">
          <a href="register.html" class="footer-link">Login</a>
          <a href="register.html" class="footer-link">Register</a>
          <a href="#" class="footer-link">About Us</a>
          <a href="#" class="footer-link">Return Policy</a>
          <a href="#" class="footer-link">Orders</a>
        </div>
        <p class="footer-paragraph">
          Copyright &copy; GymBS All Rights Reserved
        </p>
      </footer>
      <!-- End of Footer -->
    </div>

    <script src="script.js"></script>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
      crossorigin="anonymous"
    ></script>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
  </body>
</html>
