from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def display(action: dict, result: dict):
    if not result["ok"]:
        console.print(f"[red]Error:[/red] {result['error']}\n")
        return

    data = result["data"]
    service = action["service"]
    method = action["action"]

    if service == "lambda" and method == "list_functions":
        _display_lambdas(data)

    elif service == "ec2" and method == "describe_instances":
        _display_ec2(data)

    elif service == "s3" and method == "list_buckets":
        _display_s3(data)

    elif service == "iam" and method == "list_users":
        _display_iam_users(data)

    else:
        console.print(data)

def _display_lambdas(data):
    functions = data.get("Functions", [])
    if not functions:
        console.print("[yellow]No Lambda functions found.[/yellow]\n")
        return

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
    table.add_column("Name")
    table.add_column("Runtime")
    table.add_column("Memory")
    table.add_column("Last Modified")

    for fn in functions:
        table.add_row(
            fn.get("FunctionName", "—"),
            fn.get("Runtime", "—"),
            str(fn.get("MemorySize", "—")) + " MB",
            fn.get("LastModified", "—")[:10]
        )

    console.print(f"\n[bold]Lambda Functions[/bold] ({len(functions)} total)")
    console.print(table)

def _display_ec2(data):
    reservations = data.get("Reservations", [])
    instances = [i for r in reservations for i in r.get("Instances", [])]

    if not instances:
        console.print("[yellow]No EC2 instances found.[/yellow]\n")
        return

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
    table.add_column("Instance ID")
    table.add_column("Type")
    table.add_column("State")
    table.add_column("Name")

    for i in instances:
        name = next((t["Value"] for t in i.get("Tags", []) if t["Key"] == "Name"), "—")
        state = i["State"]["Name"]
        state_colored = f"[green]{state}[/green]" if state == "running" else f"[red]{state}[/red]"
        table.add_row(
            i.get("InstanceId", "—"),
            i.get("InstanceType", "—"),
            state_colored,
            name
        )

    console.print(f"\n[bold]EC2 Instances[/bold] ({len(instances)} total)")
    console.print(table)

def _display_s3(data):
    buckets = data.get("Buckets", [])

    if not buckets:
        console.print("[yellow]No S3 buckets found.[/yellow]\n")
        return

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
    table.add_column("Name")
    table.add_column("Created")

    for b in buckets:
        table.add_row(
            b.get("Name", "—"),
            str(b.get("CreationDate", "—"))[:10]
        )

    console.print(f"\n[bold]S3 Buckets[/bold] ({len(buckets)} total)")
    console.print(table)

def _display_iam_users(data):
    users = data.get("Users", [])

    if not users:
        console.print("[yellow]No IAM users found.[/yellow]\n")
        return

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
    table.add_column("Username")
    table.add_column("User ID")
    table.add_column("Created")

    for u in users:
        table.add_row(
            u.get("UserName", "—"),
            u.get("UserId", "—"),
            str(u.get("CreateDate", "—"))[:10]
        )

    console.print(f"\n[bold]IAM Users[/bold] ({len(users)} total)")
    console.print(table)