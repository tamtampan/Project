[//]: # (# Project)

[//]: # ()
[//]: # (### This is server-side web shop application for car products. )

[//]: # ()
[//]: # (## Endpoints)

[//]: # (### This is list of all database tables and almost every route. )

[//]: # ()
[//]: # (Every table have CRUD operations &#40;Create - Read by id - Read all - Update - Delete&#41;)

[//]: # (##)

[//]: # (1&#41; Users: CRUD + Create superuser + **Log in** + Update password)

[//]: # (2&#41; Customers: CRUD + **Create customer with shopping cart** + Get by phone / email)

[//]: # (3&#41; Employees: CRUD)

[//]: # (4&#41; Offices: CRUD + Get by name)

[//]: # (5&#41; Producers: CRUD + Get by name)

[//]: # (6&#41; Product categories: CRUD + Get by name like)

[//]: # (7&#41; Products: CRUD + Update quantity in stock + **Get Products by descending number of sold** + Get products for car brand + **Get products by category name** + **Get all sorted by price from lowest** + Get all sorted by price from highest + **Get all products alphabetically sorted** + Read by code + Read by name or initial letters)

[//]: # (8&#41; Shopping cart: CRUD + Get by customer id)

[//]: # (9&#41; Cart item: CRUD + Create with customer id + **Get all items for shopping cart**)

[//]: # (10&#41; Shopping order: CRUD + **Create shopping order automatically** + **Get order with items** + **Get today shopping orders** + **Sum today profit**)

[//]: # (11&#41; Shopping order items: CRUD + Get items by shopping order id)

[//]: # (#)

[//]: # ()
[//]: # (Log in with:   )

[//]: # (email: admin@itbc.rs   )

[//]: # (password: Admin123!)

[//]: # (#)

[//]: # (Easiest way to make order:)

[//]: # (- Get customer id &#40;or create one, with Create Customer with Shopping cart route&#41;)

[//]: # (###### customer:)

[//]: # (###### 058d223b-df63-4ac0-a044-b355f75d7f77)

[//]: # (- Put customer id in Create Cart Item By Customer id and add product id you like)

[//]: # (###### products:)

[//]: # (###### 20ff0e12-6ab4-4fe6-a799-d1d760781549)

[//]: # (###### 45e2b827-edc0-4306-b9ed-d2cd4ad62902)

[//]: # (###### 96b94911-a46c-4d70-933c-29d8450e0a93)

[//]: # (- Put customer id in Create Shopping Order Automatically and add office id:)

[//]: # (###### office:)

[//]: # (###### 4d1049f8-6442-4268-a4cd-f5f7279a2d0c)

# ITBC Final FastAPI project - Tamara Pantic

This is server-side web shop for car products.
The application should be able to allow login for users, who may have different roles.
After login, a user should be able to leave a personal data, see products filtered in different ways and to choose products for the wish list. At the end, customer should be able to order products from the shopping cart and track the order.









## Installation

### Create virtual environment
#### PyCharm
```bash
venv ./venv
```
#### Windows
Open Command Prompt or PowerShell, navigate to project folder and run
```bash
python -m venv ./venv
```
#### Linux/MacOS
Open terminal, navigate to project directory and run
```bash
python -m venv ./venv
```
In case that previous command didn't work, install virtualenv
```bash
pip install virtualenv
```
Run command in project directory to create virtual env
```bash
virtualenv venv
```
### Activate Virtual environment
Open terminal and navigate to project directory, than run

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate.bat          |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |

### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```
### Database
Start MySQL server and execute all commands in **_init_db/init_db.sql_**

### Environment variables
1. Create new file **_.env_**
2. Copy all consts from **env-template** to **_.env_**
3. Assign values to const in .env file


## Run server
From terminal
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)
�
