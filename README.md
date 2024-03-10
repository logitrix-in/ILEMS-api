
# Welcome to ILEMS!

The **Integrated Law Enforcement Management System (ILEMS)** stands as a robust Federal Information Management System engineered to elevate the operational efficiency of law enforcement agencies. Harnessing cutting-edge technologies such as **real-time tracking** and **predictive analytics**, **ILEMS** optimizes resource allocation, streamlines operations, and bolsters overall effectiveness.

## Folder Structure
``` 	
ILEMS-api/
│
├── ILEMSapi/                                
│   ├── __init__.py                       
│   ├── asgi.py                      
│   ├── settings.py                     
│   ├── urls.py
│	  └── wsgi.py
│          
│
├── app/                                
│   ├── migrations/                       
│   │   └── __init__.py                                       
│   ├── __init__.py                    
│   ├── admin.py                     
│   ├── models.py                     
│   ├── tests.py                          
│   └── views.py                        
│       
├── .gitignore                               
├── README.md
├── manage.py
└── requirements.txt                    
```

## **Getting Started**

### **Clone this Repository** 
 ```git clone https://github.com/logitrix-in/ILEMS-api.git```
 
### **Install System Requirements**
 ```pip install -r requirements.txt```
 
### **Configure Environment Variables**
> Generate an **.env** file in the root directory and incorporate the necessary environment variables there.

### **Database Migration**
```
python manage.py makemigrations
python manage.py migrate
```

### **Create Superuser**
```
python manage.py createsuperuser
```

### **Launch the Server**
```
python manage.py runserver
```

## **Contributing**
We welcome contributions from the community! To contribute to ILEMS, please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new Pull Request

## **Issues**
If you encounter any issues with ILEMS, please feel free to [open an issue](https://github.com/logitrix-in/ILEMS-api/issues/new) on our GitHub repository. We appreciate your feedback and will work to resolve any problems promptly.

## **License**
ILEMS is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
