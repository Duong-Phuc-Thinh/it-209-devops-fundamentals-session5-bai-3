import subprocess
import os

def run_command(command):
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

def setup_git_scenario():
    if not os.path.exists(".git"):
        run_command("git init")
    
    with open("config.json", "w") as f:
        f.write('{\n  "port": 8080,\n  "debug": false\n}')
    
    run_command("git add config.json")
    run_command('git commit -m "init config"')
    
    run_command("git checkout -b feature-api")
    
    with open("config.json", "w") as f:
        f.write('{\n  "port": 9000,\n  "debug": false\n}')
    run_command("git add config.json")
    run_command('git commit -m "feat: change port"')
    
    with open(
        "config.json", "w"
    ) as f:
        f.write('{\n  "port": 9000,\n  "debug": true\n}')
    run_command("git add config.json")
    run_command('git commit -m "feat: enable debug"')
    
    run_command("git checkout main")
    with open("config.json", "w") as f:
        f.write('{\n  "port": 8081,\n  "debug": false\n}')
    run_command("git add config.json")
    run_command('git commit -m "update port on main"')
    
    with open("config.json", "w") as f:
        f.write('{\n  "port": 8081,\n  "debug": false,\n  "env": "production"\n}')
    run_command("git add config.json")
    run_command('git commit -m "add env config"')
    
    run_command("git checkout feature-api")
    print("\nSetup completed. Now you can run: git rebase main\n")

if __name__ == "__main__":
    setup_git_scenario()
