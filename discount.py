#-Begin-----------------------------------------------------------------

#-Includes--------------------------------------------------------------
import sys, win32com.client

#-Sub Main--------------------------------------------------------------


def btn_discount(x, y):
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
                if temp_session.Info.Transaction == "VA22":
                    session = temp_session
                    break

            
            session.findById("wnd[0]/usr/ctxtVBAK-VBELN").text = line
            session.findById("wnd[0]").sendVKey(0)
            try:
                session.findById("wnd[1]/tbar[0]/btn[0]").press()
            except:
                pass
            session.findById("wnd[0]/usr/subSUBSCREEN_PARTNER:SAPMV45A:9972/txtGV_NETPR").text = y
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/tbar[0]/btn[11]").press()


        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            application = None
            SapGuiAuto = None

#-Main------------------------------------------------------------------
if __name__ == "__main__":
    btn_discount()

#-End-------------------------------------------------------------------