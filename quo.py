#-Begin-----------------------------------------------------------------

#-Includes--------------------------------------------------------------
import sys, win32com.client
import os

#-Sub Main--------------------------------------------------------------


def btn_quo(x, y):
    
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
            session.findById("wnd[0]/mbar/menu[0]/menu[5]").select()
            session.findById("wnd[1]/tbar[0]/btn[86]").press()


        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            application = None
            SapGuiAuto = None




    outlook = win32com.client.Dispatch("Outlook.Application")
    inspectors = outlook.Inspectors

 

    for inspector in inspectors:
        if inspector.CurrentItem.Class == 43: # wiadomość e-mail
            if inspector.CurrentItem.Attachments.Count > 0:
                for attachment in inspector.CurrentItem.Attachments:
                    if attachment.FileName.endswith(".pdf") or attachment.FileName.endswith(".PDF"): # sprawdzenie czy plik jest pdf
                        # attachment.SaveAsFile(os.path.join("S:\\10. Project files\\", y, "\\", attachment.FileName))
                        attachment.SaveAsFile(os.path.join(y, attachment.FileName))
            #             print("Załącznik zapisany jako " + attachment.FileName)
                    # else:
            #             print("Plik "+attachment.FileName+" nie jest plikiem pdf.")
            # else:
            #     print("Wiadomość nie posiada załączników.")

 

    while outlook.Inspectors.Count > 0:
        for inspector in outlook.Inspectors:
            inspector.Close(0)
        continue
            
    


#-Main------------------------------------------------------------------
if __name__ == "__main__":
    btn_quo()

#-End-------------------------------------------------------------------