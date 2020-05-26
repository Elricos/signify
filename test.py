import os
import sys

try:
    from signify.signed_pe import SignedPEFile
    from signify.context import VerificationContext
    from signify.certificates import Certificate
    from signify.exceptions import AuthenticodeVerificationError
except:
    print("import error in test")

def main():
    data_file = sys.argv[1]
    try:
        with open(data_file, 'rb') as objf:
            pefile = SignedPEFile(objf)
            try:
                pefile.verify()
            except AuthenticodeVerificationError:
                print("could not verify cert")
            except Exception as error:
                print("error with verify")
                print(error.__class__.__name__ + ": " + error.message)
                return{}

            for signed_data in pefile.signed_datas:
                print(signed_data.signer_info.program_name)
                for cert in signed_data.certificates:
                    print(cert)
    except Exception as error:
        print("Gen error")
        print(error.__class__.__name__ + ": " + error.message)

main()