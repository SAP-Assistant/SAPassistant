#-Begin-----------------------------------------------------------------

#-Includes--------------------------------------------------------------
import sys, win32com.client

#-Sub Main--------------------------------------------------------------


def btn_xml(x, y):
    for line in x:

        try:

            SapGuiAuto = win32com.client.GetObject("SAPGUISERVER")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                return

            application = SapGuiAuto.GetScriptingEngine
            if not type(application) == win32com.client.CDispatch:
                SapGuiAuto = None
                return

            connection = application.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                application = None
                SapGuiAuto = None
                return

            session = None
            for i in range(connection.Children.Count):
                temp_session = connection.Children(i)
                if temp_session.Info.Transaction == "ZSDVC_XML":
                    session = temp_session
                    break

            
            session.findById("wnd[0]/usr/radP_DLOAD").select()
            session.findById("wnd[0]/usr/txtP_VBELN").text = line
            session.findById("wnd[0]/usr/ctxtP_FILE").text = f"{y}\{line}-xml.xml"
            session.findById("wnd[0]/tbar[1]/btn[8]").press()


        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            application = None
            SapGuiAuto = None

#-Main------------------------------------------------------------------
if __name__ == "__main__":
    btn_xml()

#-End-------------------------------------------------------------------