from src.data_cleaner import clean_data
from src.excel_exporter import export_to_template

def main():
    # 配置文件路径
    input_file = "data/sample_data.xlsx"
    template_file = "data/result_template.xlsx"
    output_file = "data/cleaned_result.xlsx"

    try:
        print("开始读取并清洗数据……")
        clean_df = clean_data(input_file)
        print(f"清洗完成，一共剩余 {len(clean_df)} 条数据")

        print("正在写入模板……")
        export_to_template(clean_df, template_file, output_file)
        print(f"✅ 全部完成！结果保存在：{output_file}")

    except Exception as e:
        print(f"❌ 程序出错：{e}")
        # 错误信息写入日志
        with open("log/debug_record.md", "a", encoding="utf-8") as f:
            f.write(f"\n【报错】{e}\n")

if __name__ == "__main__":
    main()
