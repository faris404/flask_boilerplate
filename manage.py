import typer
import os

app = typer.Typer()


@app.command()
def migrate():
    #check a folder already exists by name
    is_exist = os.path.exists(os.path.join(os.getcwd(), 'migrations'))
    if is_exist:
         print(f'migrations folder already exists')
         # execute the command migrate and upgrade
         os.system('python3 -m flask db migrate')
         os.system('python3 -m flask db upgrade')
         print(f'migration success')

    else:
         print(f'migrations folder not found')
         print(f'creating migrations')
         #  creating db init command
         os.system('python3 -m flask db init')
         print(f'migration folder created')
         # execute the command migrate and upgrade
         os.system('python3 -m flask db migrate')
         os.system('python3 -m flask db upgrade')
         print(f'migration success')

@app.command()
def resource(name: str):
    # create a folder with name from the command in resource folder
    os.system(f'mkdir resources/{name}')
    os.system(f'touch resources/{name}/urls.py')
    os.system(f'touch resources/{name}/__init__.py')
    typer.echo(f"created")



if __name__ == "__main__":
    app()