@servers(['web' => 'localhost'])

@setup
    $PROJECT_ROOT = "/var/www/inkomoko";
    $BRANCH = 'main';
@endsetup

@task('deploy')
    cd {{ $PROJECT_ROOT }}
    git pull origin {{ $BRANCH }}
    docker compose down -v
    docker compose up -d --build --force-recreate
    echo "MESSAGE => Deployment complete!"
@endtask
