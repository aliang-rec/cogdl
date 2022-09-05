from cogdl import options, experiment


if __name__ == "__main__":
    parser = options.get_training_parser()                  # 获取参数
    args, _ = parser.parse_known_args()
    args = options.parse_args_and_arch(parser, args)        # 参数解析

    experiment(dataset=args.dataset, model=args.model, args=args)       # 实验
