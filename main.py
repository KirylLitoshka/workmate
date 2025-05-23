from src.args import get_arguments
from src.files import get_files_data
from src.reports import build_report

def main():
    args = get_arguments()
    data = get_files_data(args.files)
    build_report(args.report, data)



if __name__ == "__main__":
    main()
