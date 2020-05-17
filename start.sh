echo $SOCKFILE

SOCKFILEDIR="$(dirname "$SOCKFILE")"
VENV_ACTIVATE=${VENV_BIN}"/activate"
VENV_GUNICORN=${VENV_BIN}"/gunicorn"

# Activate the virtual environment.
cd $BASEDIR
source $VENV_ACTIVATE
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$PYTHONPATH:$BASEDIR

# Create run directory if they does not exists.
test -d $SOCKFILEDIR || mkdir -p $SOCKFILEDIR

# Start Gunicorn!
# Programs meant to be run under supervisor should not daemonize themselves
# (do not use --daemon).
exec ${VENV_GUNICORN} ${DJANGO_WSGI_MODULE}:application \
       --bind=unix:$SOCKFILE \
       --name $NAME \
       --workers $NUM_WORKERS