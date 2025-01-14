import sys
import time

# Try to stop infinite loop that occurs because (I think) 
# scanpy uses the multiprocessing library which does not 
# always play nicely with pyinstaller
# https://github.com/pyinstaller/pyinstaller/issues/2322#issuecomment-699603755

# This prevents an infinite loop of starting new instances
# but leaves two glue processes running.
import multiprocessing
multiprocessing.freeze_support()
multiprocessing.set_start_method('spawn')

from glue import load_plugins
from glue.logger import logger
from glue.app.qt import GlueApplication


logger.setLevel("INFO")

load_plugins()

if __name__ == "__main__":

    if "--debug" in sys.argv:
        import faulthandler

        faulthandler.enable()

    for arg in sys.argv:
        if arg.endswith(".glu"):
            session = arg
            break
    else:
        session = None

    if session:

        ga = GlueApplication.restore_session(session)
        ga.app.exec_()

    else:

        ga = GlueApplication()

        if "--test" in sys.argv:

            ga.start(block=False)

            # Open a few viewers to test

            from glue.viewers.image.qt import ImageViewer

            ga.new_data_viewer(ImageViewer)

            from glue_vispy_viewers.scatter.scatter_viewer import VispyScatterViewer

            ga.new_data_viewer(VispyScatterViewer)

            start = time.time()
            print("Waiting 5 seconds before closing...")
            while time.time() - start < 5:
                ga.app.processEvents()

        else:
            ga.start()
