@servers(['web' => 'localhost'])

@setup
    $PROJECT_ROOT = "/var/www/inkomoko";
    $BRANCH = 'main';
@endsetup

@task('deploy')
    cd {{ $PROJECT_ROOT }}
    git pull origin {{ $BRANCH }}
    echo "MESSAGE => Deployment complete!"
@endtask
