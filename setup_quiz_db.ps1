# setup_quiz_db.ps1

$dbFile = "quiz.db"
$createTablesScript = "create_quiz_tables.sql"
$insertDataScript = "insert_quiz_data.sql"

Write-Host "Starting database setup..."

# 1. Delete existing database file
if (Test-Path $dbFile) {
    Write-Host "Deleting existing database: $dbFile"
    try {
        Remove-Item $dbFile -Force -ErrorAction Stop
        Write-Host "Successfully deleted $dbFile."
    } catch {
        Write-Host "Remove-Item : $($_.Exception.Message)"
        Write-Host "Error: Could not delete $dbFile. Ensure no other applications (like your Python app or DB Browser for SQLite) are using it."
        exit 1 # Exit with an error code
    }
} else {
    Write-Host "Database file $dbFile not found. Proceeding with creation."
}

# 2. Create tables
Write-Host "Creating database tables from $createTablesScript..."
try {
    # Use Get-Content and pipe to sqlite3 for PowerShell compatibility
    Get-Content $createTablesScript | sqlite3 $dbFile
    Write-Host "Database tables created successfully."
} catch {
    Write-Host "Error creating database tables: $($_.Exception.Message)"
    exit 1
}

# 3. Insert data
Write-Host "Inserting data into tables from $insertDataScript..."
try {
    # Use Get-Content and pipe to sqlite3 for PowerShell compatibility
    Get-Content $insertDataScript | sqlite3 $dbFile
    Write-Host "Data inserted successfully."
} catch {
    Write-Host "Error inserting data: $($_.Exception.Message)"
    exit 1
}

Write-Host "Database setup complete."