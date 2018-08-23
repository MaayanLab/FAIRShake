# FAIRshake

A web interface for the scoring of biomedical digital objects by user evaluation according to the FAIR data principles: Findability, Accessibility, Interoperability, and Reusability.

Available at http://fairshake.cloud/

## Code Layout
- FAIRshake: The django project settings
- FAIRshakeHub: The website itself, gets all of its information from FAIRshakeAPI
- FAIRshakeAPI: The primary API facilitator, is enabled with the other API components
- extensions: Extensions to dependent libraries

## Development

### Setup
Python 3 is required to run this project.

Install all dependencies into your environment.
```bash
pip install -r requirements.txt
```

Note that `mysqlclient` is the recommended client but `pymysql` can be used as a fallback.

### Django Shell
ipython is recommended: `pip install ipython`
`./manage.py shell`

### Django Live Reloading Server
In separate terminals execute these commands and then navigate to <http://localhost:8000/v2/>.
```bash
./manage.py runserver
./manage.py livereload
```

### Build Docker
```bash
docker-compose build
```

### Database migrations
Django keeps track of database migrations. When modifying `models` it is imperative to create and apply migrations on all old databases. Migrations can be safely removed if they have been applied to all independent databases (for that reason, it's probably better to just not remove them).
```bash
./manage.py makemigrations
./manage.py migrate
```

Note that this will try but not always succeed to detect renamed fields and such and migrate the backend database accordingly. If it is unable to, it may require manual intervention. For more information https://docs.djangoproject.com/en/2.0/topics/migrations/.

## Production
### Secret values
For the docker-compose to work properly in production, `/ssl/` should have the following files:
- `my.cnf`: mysql configuration file with production database credentials
  - This file can be specified with `MYSQL_CONFIG` environment variable
- `secret.txt`: Secret key for production (random private string of characters)
- `cert.key`: SSL Private Key
- `cert.crt`: SSL CA Signed Public Key

### Email
Can be configured by the administrator [here](http://localhost:8000/v2/admin/des/dynamicemailconfiguration/). If using gmail, ensure you [allow less secure apps](https://myaccount.google.com/lesssecureapps).

### Docker deployment
```bash
docker-compose up
```

## Troubleshooting

### MySQL issues
Errors involving mysql trying to load from /tmp/sock arrise when `MYSQL_CONFIG` environment variable is being read, but the file on the other end is problematic.
1. You're not using an absolute path, so django, running perhaps elsewhere, can't find it. Try: `export MYSQL_CONFIG=$(pwd)/ssl/my.cnf`
  - Verify that it's accessible at the environment variable with `cat $MYSQL_CONFIG`
2. Your configuration file has loose permissions, Try: `chmod 644 ssl/my.cnf` before trying again.
3. Your configuration is malformed.

### Database issues
In general, if the database has changed (and there are new migration files), if you're running a local database you may need to apply new migrations with `./manage.py migrate`.

### Dependency issues
First try re-executing `pip install -r requirements.txt`.

In the worst case you may need to rebuild your environment from nothing (starting from scratch, and installing dependencies again).

I recommend `pyenv` for managing isolated python environments.
