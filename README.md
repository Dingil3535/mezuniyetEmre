# Climate Change Awareness Website

A comprehensive Flask-based web application dedicated to educating people about climate change through science-based articles, practical solutions, and actionable information.

## 🌍 About

Climate Change Awareness is a web platform that provides accurate, science-based information about climate change to help people understand the challenges we face and the solutions available. The platform features articles covering various aspects of climate science, impacts, and solutions, with an emphasis on making complex information accessible to everyone.

## ✨ Features

### Public Features
- **Homepage**: Overview with featured articles and climate change facts
- **Article System**: Browse and read climate change articles by category
- **Categories**: Science, Solutions, and Impact articles
- **Responsive Design**: Modern, mobile-friendly interface
- **About Page**: Information about the platform's mission and values
- **Contact Page**: Get in touch with the team

### Admin Features
- **User Authentication**: Login and registration system
- **Admin Panel**: Manage articles and content
- **Article Creation**: Create new climate change articles
- **Content Management**: Edit and organize existing content

### Content Categories
- **Science**: Understanding the science behind climate change
- **Solutions**: Renewable energy, individual actions, and mitigation strategies
- **Impact**: Effects of climate change on weather, ecosystems, and society

## 🚀 Getting Started

### Prerequisites
- Python 3.13
- pipenv (for dependency management)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd climate-change
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Access the website**
   - Open your browser and go to `http://127.0.0.1:5001`
   - The database will be automatically created and populated with initial content

## 📁 Project Structure

```
climate-change/
├── main.py                 # Main Flask application
├── Pipfile                 # Python dependencies
├── Pipfile.lock           # Locked dependency versions
├── README.md              # Project documentation
├── instance/              # Database files
│   └── climate_change.db  # SQLite database
├── static/                # Static assets
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   └── img/               # Images and icons
│       ├── climate-logo.svg
│       ├── earth-icon.svg
│       └── ...
└── templates/             # HTML templates
    ├── home.html          # Homepage
    ├── articles.html      # Articles listing
    ├── article.html       # Individual article view
    ├── about.html         # About page
    ├── contact.html       # Contact page
    ├── login.html         # Login form
    ├── registration.html  # User registration
    ├── admin.html         # Admin panel
    └── create_article.html # Article creation form
```

## 🗄️ Database Schema

### ClimateArticle Model
- `id`: Primary key
- `title`: Article title
- `subtitle`: Article subtitle/description
- `content`: Full article content
- `category`: Article category (Science, Solutions, Impact)
- `date_created`: Creation timestamp
- `author`: Article author

### User Model
- `id`: Primary key
- `email`: User email (unique)
- `password`: User password
- `name`: User's full name
- `date_joined`: Registration timestamp

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Responsive Design
- **Dependencies**: Flask-SQLAlchemy
- **Development**: Python 3.13, pipenv

## 📝 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Homepage with featured articles |
| GET | `/articles` | Articles listing (with optional category filter) |
| GET | `/article/<id>` | Individual article view |
| GET | `/about` | About page |
| GET | `/contact` | Contact page |
| GET/POST | `/login` | User login |
| GET/POST | `/register` | User registration |
| GET | `/admin` | Admin panel (requires authentication) |
| GET/POST | `/create_article` | Create new article (requires authentication) |

## 🎨 Customization

### Adding New Articles
1. Log in to the admin panel
2. Click "Create New Article"
3. Fill in the article details:
   - Title and subtitle
   - Content (supports HTML formatting)
   - Category (Science, Solutions, or Impact)
   - Author name

### Styling
- Modify `static/css/style.css` to customize the appearance
- The design is responsive and mobile-friendly
- Uses modern CSS with flexbox and grid layouts

### Content Categories
You can add new categories by:
1. Modifying the category options in `create_article.html`
2. Updating the category filter in `articles.html`
3. Adding category-specific styling if needed

## 🌱 Sample Content

The application comes pre-populated with comprehensive articles covering:

1. **Understanding Global Warming** - The science behind rising temperatures
2. **Renewable Energy Solutions** - Clean energy technologies and their benefits
3. **Climate Change and Extreme Weather** - How global warming affects weather patterns
4. **Individual Actions for Climate Change** - Practical steps people can take

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Climate science data and research from leading scientific organizations
- Flask community for excellent documentation and resources
- Environmental organizations working to combat climate change

## 📞 Support

If you have any questions or need help with the project, please:
- Open an issue on GitHub
- Contact us through the website's contact page
- Check the documentation and FAQ sections

---

**Remember**: Climate change is one of the most pressing challenges of our time. This platform aims to educate and empower people to take meaningful action. Every small step counts in building a more sustainable future.

🌍 **Together, we can make a difference!** 🌍
