import os
import sys

from signify.signed_pe import SignedPEFile
from signify.context import VerificationContext
from signify.certificates import Certificate
from signify.exceptions import AuthenticodeVerificationError

def main():
    data_file = sys.argv[1]

    with open(data_file, 'rb') as objf:
        pefile = SignedPEFile(objf)
        try:
            pefile.verify()
        except AuthenticodeVerificationError:
            print("could not verify cert")
        except:
            print(sys.exc_info()[0])
            return {}

        for signed_data in pefile.signed_datas:
            print(signed_data.signer_info.program_name)
            for cert in signed_data.certificates:
                print(cert)

main()