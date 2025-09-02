# 🚀 Deployment Guide - Jugglers Shop

Complete step-by-step guide to deploy the e-commerce platform.

## 📋 Prerequisites

- GitHub account
- Vercel account (free)
- Render account (free)
- Domain name (optional)

## 🔧 Backend Deployment (Render)

### Step 1: Prepare Repository
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the `backend` folder
5. Configure:
   - **Name**: `jugglers-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn backend.wsgi:application`

### Step 3: Environment Variables
Add these in Render dashboard:
```
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=jugglers-backend.onrender.com
DATABASE_URL=postgresql://... (auto-generated)
```

### Step 4: Database Setup
1. Create PostgreSQL database on Render
2. Connect to web service
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`

## 🌐 Frontend Deployment (Vercel)

### Customer Frontend

#### Step 1: Deploy Main Site
1. Go to [vercel.com](https://vercel.com)
2. Import from GitHub
3. Select `jugglers-shop` folder
4. Configure:
   - **Framework**: Vite
   - **Root Directory**: `jugglers-shop`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

#### Step 2: Environment Variables
```
VITE_API_URL=https://jugglers-backend.onrender.com
```

### Admin Panel

#### Step 1: Deploy Admin Dashboard
1. Create new Vercel project
2. Select `admin-panel` folder
3. Same configuration as main site

#### Step 2: Environment Variables
```
VITE_API_URL=https://jugglers-backend.onrender.com
```

## 🔗 Domain Configuration

### Custom Domains (Optional)
1. **Main Site**: `jugglers.shop`
2. **Admin Panel**: `admin.jugglers.shop`
3. **API**: `api.jugglers.shop`

### DNS Settings
```
Type: CNAME
Name: @
Value: jugglers-shop.vercel.app

Type: CNAME  
Name: admin
Value: jugglers-admin.vercel.app

Type: CNAME
Name: api  
Value: jugglers-backend.onrender.com
```

## 🔒 Security Configuration

### Backend CORS Update
Update `settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "https://jugglers.shop",
    "https://admin.jugglers.shop",
    "https://jugglers-shop.vercel.app",
    "https://jugglers-admin.vercel.app",
]
```

### Environment Variables Security
- Never commit `.env` files
- Use strong SECRET_KEY
- Set DEBUG=False in production
- Use HTTPS URLs only

## 📊 Post-Deployment Checklist

### Backend Verification
- [ ] API endpoints working
- [ ] Admin panel accessible
- [ ] Database migrations applied
- [ ] Static files serving
- [ ] CORS configured correctly

### Frontend Verification
- [ ] Main site loading
- [ ] Admin panel loading
- [ ] API calls working
- [ ] Authentication working
- [ ] Images loading correctly

### Functionality Testing
- [ ] User registration/login
- [ ] Product browsing
- [ ] Add to cart
- [ ] Place order
- [ ] Admin order management
- [ ] Product management

## 🚨 Troubleshooting

### Common Issues

#### Backend Issues
```bash
# Check logs
render logs

# Database connection
python manage.py dbshell

# Static files
python manage.py collectstatic
```

#### Frontend Issues
```bash
# Build locally
npm run build

# Check environment variables
echo $VITE_API_URL

# Network requests
Check browser dev tools → Network tab
```

### Error Solutions

#### CORS Errors
- Update ALLOWED_HOSTS in Django
- Check CORS_ALLOWED_ORIGINS
- Verify API URL in frontend

#### Database Errors
- Check DATABASE_URL
- Run migrations
- Verify PostgreSQL connection

#### Build Errors
- Check Node.js version
- Clear node_modules and reinstall
- Verify environment variables

## 📈 Performance Optimization

### Backend
- Enable gzip compression
- Use CDN for static files
- Database query optimization
- Caching implementation

### Frontend
- Image optimization
- Code splitting
- Lazy loading
- Bundle size optimization

## 🔄 CI/CD Pipeline (Optional)

### GitHub Actions
```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
```

## 📱 Mobile App (Future)

### React Native Setup
- Expo CLI installation
- API integration
- Push notifications
- App store deployment

## 🎯 Production URLs

After deployment, your URLs will be:

- **Main Site**: https://jugglers-shop.vercel.app
- **Admin Panel**: https://jugglers-admin.vercel.app  
- **API Backend**: https://jugglers-backend.onrender.com

## 📞 Support

For deployment issues:
- **Email**: siddharthjinigam@gmail.com
- **Phone**: +91 9098613462
- **GitHub**: Create an issue in the repository

---

**Happy Deploying! 🚀**