# Climate Change Website
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# SQLite database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///climate_change.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Climate Article Model
class ClimateArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., "Science", "Solutions", "Impact"
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(100), nullable=False, default="Climate Team")

    def __repr__(self):
        return f'<ClimateArticle {self.id}>'

# User Model for community features
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)



# Home page - Climate Change Overview
@app.route('/')
def home():
    # Get featured articles
    featured_articles = ClimateArticle.query.order_by(ClimateArticle.date_created.desc()).limit(3).all()
    return render_template('home.html', articles=featured_articles)

# Articles listing page
@app.route('/articles')
def articles():
    category = request.args.get('category', 'all')
    if category == 'all':
        articles = ClimateArticle.query.order_by(ClimateArticle.date_created.desc()).all()
    else:
        articles = ClimateArticle.query.filter_by(category=category).order_by(ClimateArticle.date_created.desc()).all()
    return render_template('articles.html', articles=articles, current_category=category)

# Individual article page
@app.route('/article/<int:id>')
def article(id):
    article = ClimateArticle.query.get_or_404(id)
    # Get related articles
    related_articles = ClimateArticle.query.filter(
        ClimateArticle.category == article.category,
        ClimateArticle.id != id
    ).limit(3).all()
    return render_template('article.html', article=article, related_articles=related_articles)

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']
        
        # User authentication
        users_db = User.query.all()
        for user in users_db:
            if form_login == user.email and form_password == user.password:
                return redirect('/admin')
        error = 'Invalid email or password'
        return render_template('login.html', error=error)    
    else:
        return render_template('login.html')   
  
# Registration page
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            error = 'Email already registered'
            return render_template('registration.html', error=error)
        
        # Create new user
        user = User(email=email, password=password, name=name)
        db.session.add(user)    
        db.session.commit()
        return redirect('/login')
    else:    
        return render_template('registration.html')

# Admin panel for creating articles
@app.route('/admin')
def admin():
    articles = ClimateArticle.query.order_by(ClimateArticle.date_created.desc()).all()
    return render_template('admin.html', articles=articles)

# Create new article
@app.route('/create_article', methods=['GET','POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        content = request.form['content']
        category = request.form['category']
        author = request.form['author']

        # Create new article
        article = ClimateArticle(
            title=title, 
            subtitle=subtitle, 
            content=content, 
            category=category,
            author=author
        )

        db.session.add(article)
        db.session.commit()
        return redirect('/admin')
    else:
        return render_template('create_article.html')

# Function to populate database with initial climate change content
def populate_database():
    # Check if articles already exist
    if ClimateArticle.query.count() == 0:
        initial_articles = [
            ClimateArticle(
                title="Understanding Global Warming",
                subtitle="The science behind rising global temperatures and their impact on our planet",
                content="""Global warming refers to the long-term increase in Earth's average surface temperature due to greenhouse gas emissions from human activities. Since the late 19th century, Earth's average temperature has risen by about 1.1°C (2°F).

The primary cause is the burning of fossil fuels (coal, oil, and natural gas), which releases carbon dioxide and other greenhouse gases into the atmosphere. These gases trap heat from the sun, creating a 'greenhouse effect.'

Key impacts include:
• Rising sea levels due to thermal expansion and melting ice
• More frequent and intense extreme weather events
• Ocean acidification affecting marine ecosystems
• Shifts in precipitation patterns
• Threats to biodiversity and food security

The scientific consensus is clear: human activities are the dominant cause of observed warming since the mid-20th century. Immediate action is needed to reduce emissions and limit global temperature rise to 1.5°C above pre-industrial levels.""",
                category="Science",
                author="Climate Research Team"
            ),
            ClimateArticle(
                title="Renewable Energy Solutions",
                subtitle="How clean energy technologies can help combat climate change",
                content="""Renewable energy sources offer a sustainable path forward in the fight against climate change. These technologies harness natural processes that are constantly replenished, providing clean alternatives to fossil fuels.

Solar Power:
• Photovoltaic cells convert sunlight directly into electricity
• Costs have dropped 85% since 2010
• Can be deployed at utility scale or distributed on rooftops

Wind Energy:
• Onshore and offshore wind farms generate clean electricity
• Technology improvements have increased efficiency and reduced costs
• Provides reliable power when combined with energy storage

Hydropower:
• Uses flowing water to generate electricity
• Provides consistent, dispatchable power
• Can be combined with pumped storage for grid stability

Other promising technologies include geothermal energy, biomass, and emerging solutions like tidal and wave power. The key is creating an integrated energy system that combines multiple renewable sources with smart grid technology and energy storage.

Investment in renewable energy has grown dramatically, with global capacity increasing by 45% in 2020 alone. This transition not only reduces emissions but also creates jobs, improves air quality, and enhances energy security.""",
                category="Solutions",
                author="Energy Innovation Team"
            ),
            ClimateArticle(
                title="Climate Change and Extreme Weather",
                subtitle="How global warming is intensifying storms, droughts, and heatwaves",
                content="""Climate change is making extreme weather events more frequent, intense, and destructive. As global temperatures rise, the atmosphere can hold more moisture, leading to heavier rainfall and more powerful storms.

Hurricanes and Typhoons:
• Warmer ocean temperatures fuel more intense storms
• Rising sea levels increase storm surge damage
• Storms are moving slower, causing more prolonged impacts

Heatwaves:
• Record-breaking temperatures are becoming more common
• Urban heat islands amplify the effects
• Heat-related deaths are increasing globally

Droughts and Wildfires:
• Higher temperatures increase evaporation rates
• Drier conditions create fuel for wildfires
• Water scarcity affects agriculture and communities

Flooding:
• Heavier rainfall overwhelms drainage systems
• Sea level rise increases coastal flooding risk
• Flash floods are becoming more common

These extreme events have cascading effects on:
• Agriculture and food security
• Infrastructure and transportation
• Public health and safety
• Economic stability
• Ecosystem health

Adaptation measures include improved early warning systems, resilient infrastructure design, and community preparedness programs. However, reducing greenhouse gas emissions remains the most effective long-term solution.""",
                category="Impact",
                author="Climate Impact Research"
            ),
            ClimateArticle(
                title="Individual Actions for Climate Change",
                subtitle="How you can make a difference in the fight against global warming",
                content="""While systemic change is essential, individual actions collectively make a significant impact. Here are practical steps you can take to reduce your carbon footprint:

Transportation:
• Use public transit, biking, or walking when possible
• Choose electric or hybrid vehicles
• Combine errands to reduce trips
• Consider carpooling or ride-sharing

Energy at Home:
• Switch to LED light bulbs
• Use programmable thermostats
• Insulate your home properly
• Choose energy-efficient appliances
• Consider solar panels or renewable energy plans

Diet and Food:
• Reduce meat consumption, especially beef
• Buy local and seasonal produce
• Minimize food waste
• Choose organic when possible
• Grow your own vegetables

Consumption Habits:
• Buy less, choose quality over quantity
• Repair items instead of replacing them
• Choose products with minimal packaging
• Support companies with sustainable practices
• Reduce, reuse, and recycle

Advocacy:
• Vote for climate-conscious leaders
• Support environmental organizations
• Educate others about climate change
• Participate in community climate initiatives
• Use your voice on social media

Remember: Small actions add up. The most important step is to start somewhere and build sustainable habits over time.""",
                category="Solutions",
                author="Climate Action Team"
            )
        ]
        
        for article in initial_articles:
            db.session.add(article)
        
        db.session.commit()
        print("Database populated with initial climate change content!")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        populate_database()
 
    app.run(host="127.0.0.1", port=5001, debug=True)

