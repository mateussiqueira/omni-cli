"""AWS management commands for Omni CLI."""

from __future__ import annotations

from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.executor import run_command

app = typer.Typer(help="Manage AWS resources via AWS CLI")
console = Console()


def _check_aws_cli() -> None:
    """Check if AWS CLI is installed."""
    result = run_command(["aws", "--version"], timeout=10)
    if not result.success:
        console.print("[red]❌ AWS CLI is not installed.[/red]")
        console.print("[dim]Install it from: https://docs.aws.amazon.com/cli/[/dim]")
        raise typer.Exit(1)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """AWS management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni AWS[/bold blue] - Use [cyan]omni aws --help[/cyan]"))


@app.command("s3")
def s3_list(
    bucket: Optional[str] = typer.Option(None, "--bucket", "-b", help="Bucket name prefix"),
) -> None:
    """List S3 buckets."""
    _check_aws_cli()

    cmd = ["aws", "s3api", "list-buckets", "--query", "Buckets[].Name", "--output", "table"]
    result = run_command(cmd, timeout=60)

    if result.success:
        console.print(result.stdout)
    else:
        console.print(f"[red]❌ Failed to list S3 buckets[/red]")
        console.print(result.stderr)


@app.command("ec2")
def ec2_list(
    region: Optional[str] = typer.Option(None, "--region", "-r", help="AWS region"),
) -> None:
    """List EC2 instances."""
    _check_aws_cli()

    cmd = ["aws", "ec2", "describe-instances", "--query", "Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType,PublicIpAddress]", "--output", "table"]
    if region:
        cmd.extend(["--region", region])

    result = run_command(cmd, timeout=60)

    if result.success:
        console.print(result.stdout)
    else:
        console.print(f"[red]❌ Failed to list EC2 instances[/red]")
        console.print(result.stderr)


@app.command("route53")
def route53_list(
    hosted_zone: Optional[str] = typer.Option(None, "--zone", "-z", help="Hosted zone ID"),
) -> None:
    """List Route53 hosted zones or records."""
    _check_aws_cli()

    if hosted_zone:
        cmd = ["aws", "route53", "list-resource-record-sets", "--hosted-zone-id", hosted_zone, "--output", "table"]
    else:
        cmd = ["aws", "route53", "list-hosted-zones", "--query", "HostedZones[].Name", "--output", "table"]

    result = run_command(cmd, timeout=60)

    if result.success:
        console.print(result.stdout)
    else:
        console.print(f"[red]❌ Failed to list Route53 records[/red]")
        console.print(result.stderr)


@app.command("status")
def status() -> None:
    """Check AWS CLI status and configured identity."""
    _check_aws_cli()

    result = run_command(["aws", "sts", "get-caller-identity", "--output", "json"], timeout=30)

    if result.success:
        console.print("[green]✅ AWS CLI is authenticated[/green]")
        console.print(result.stdout)
    else:
        console.print("[red]❌ AWS CLI is not authenticated[/red]")
        console.print("[dim]Run [cyan]aws configure[/cyan] to set up credentials.[/dim]")
        console.print(result.stderr)
