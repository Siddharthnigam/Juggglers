# 🛒 Jugglers Shop - Complete E-commerce Platform

A full-stack e-commerce platform built with React, Django, and modern web technologies. Designed for Indian consumers with ₹ pricing and local contact details.

## 🌟 Features

### Customer Features
- 🛍️ Product browsing with categories and filters
- 🛒 Shopping cart with quantity management
- ❤️ Wishlist functionality
- 👤 User authentication (login/register)
- 📦 Order tracking and history
- 💳 Cash on Delivery (COD) payment
- 📱 Responsive design for mobile/desktop

### Admin Features
- 📊 Dashboard with sales analytics
- 📦 Product management (CRUD operations)
- 🛒 Order management with status updates
- 👥 User management
- 📈 Real-time notifications

## 🚀 Tech Stack

### Frontend
- **React 18** with TypeScript
- **Vite** for build tooling
- **Tailwind CSS** for styling
- **React Query** for data fetching
- **React Router** for navigation
- **Framer Motion** for animations
- **Lucide React** for icons

### Backend
- **Django 4.2** with Django REST Framework
- **SQLite** database (production ready)
- **JWT Authentication**
- **CORS** enabled for frontend integration
- **Python 3.11+**

## 📁 Project Structure

```
E-commerce/
├── jugglers-shop/          # Main customer frontend
├── admin-panel/            # Admin dashboard frontend
├── backend/                # Django REST API
└── README.md
```

## 🛠️ Local Development Setup

### Prerequisites
- Node.js 18+
- Python 3.11+
- Git

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Setup
```bash
# Customer Frontend
cd jugglers-shop
npm install
npm run dev

# Admin Panel
cd admin-panel
npm install
npm run dev
```

## 🌐 Deployment

### Frontend Deployment (Vercel)

#### Customer Frontend
1. Push code to GitHub
2. Connect to Vercel
3. Deploy from `jugglers-shop` folder
4. Set environment variables:
   ```
   VITE_API_URL=https://your-backend-url.onrender.com
   ```

#### Admin Panel
1. Deploy from `admin-panel` folder
2. Set environment variables:
   ```
   VITE_API_URL=https://your-backend-url.onrender.com
   ```

### Backend Deployment (Render)

1. Create `render.yaml` in backend folder
2. Set environment variables on Render:
   ```
   DJANGO_SETTINGS_MODULE=backend.settings
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-domain.onrender.com
   ```
3. Deploy from GitHub

## 📊 Database Schema

### Products
- ID, Name, Description, Price (₹)
- Category, Image URL, Stock
- Featured flag, Created date

### Orders
- ID, User, Total Amount, Status
- Shipping Address, Created date
- Order Items (Product, Quantity, Price)

### Users
- Django User model extended
- Role field (user/admin)
- Authentication via JWT

## 🔧 Configuration

### Environment Variables

#### Frontend (.env)
```
VITE_API_URL=http://127.0.0.1:8000
```

#### Backend (.env)
```
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## 📱 API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration

### Products
- `GET /api/products/` - List all products
- `GET /api/products/{id}/` - Get product details
- `POST /api/products/` - Create product (admin)

### Orders
- `GET /api/orders/` - User orders
- `POST /api/orders/create/` - Create new order
- `GET /api/orders/admin/` - All orders (admin)

## 🎨 Design Features

### Indian Localization
- ₹ (Rupee) currency throughout
- Indian address format (PIN codes)
- Contact: +91 7415159952
- Email: jugglers.shop@gmail.com
- Address: Freeganj, Ujjain, MP 456010

### Responsive Design
- Mobile-first approach
- Touch-friendly interface
- Optimized for Indian users

## 🔒 Security Features

- JWT token authentication
- CORS protection
- Input validation
- SQL injection protection
- XSS protection

## 📈 Performance

- Lazy loading for images
- Code splitting
- Optimized bundle size
- Fast API responses
- Caching strategies

## 🚀 Live Demo

- **Customer Site**: [Deploy on Vercel]
- **Admin Panel**: [Deploy on Vercel]
- **API Backend**: [Deploy on Render]

## 👥 Team

- **Developer**: Siddharth Nigam
- **Contact**: siddharthjinigam@gmail.com
- **Phone**: +91 9098613462

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

**Made with ❤️ in India 🇮🇳**