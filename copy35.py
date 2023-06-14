#-Begin-----------------------------------------------------------------

#-Includes--------------------------------------------------------------
import sys, win32com.client

#-Sub Main--------------------------------------------------------------


def btn_copy(x):
    
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
                if temp_session.Info.Transaction == "VA21":
                    session = temp_session
                    break


            
            session.findById("wnd[0]/tbar[1]/btn[8]").press()
            session.findById("wnd[1]/usr/tabsMYTABSTRIP/tabpRANG").select()
            session.findById("wnd[1]/usr/tabsMYTABSTRIP/tabpRANG/ssubSUB1:SAPLV45C:0301/ctxtLV45C-VBELN").text = line
            session.findById("wnd[1]/tbar[0]/btn[5]").press()
            session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV45A:9961/cmbVBAK-LIFSK").key = "35"
            session.findById("wnd[0]/tbar[0]/btn[11]").press()
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
            


        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            application = None
            SapGuiAuto = None

#-Main------------------------------------------------------------------
if __name__ == "__main__":
    btn_copy()

#-End-------------------------------------------------------------------