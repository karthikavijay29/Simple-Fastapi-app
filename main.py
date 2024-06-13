import todo.py
def main():
    parser=create_parser()
    args=parser.parse_args()
    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()

if __name__=="__main__":
    main()