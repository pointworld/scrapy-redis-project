import json


class JdPipeline(object):
    def process_item(self, item, spider):
        with open('jdbook.txt', 'a') as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
            f.write('\n')
        return item


class DangPipeline(object):
    def process_item(self, item, spider):
        with open('dangbook.txt', 'a') as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
            f.write('\n')
        return item


class AmazonPipeline(object):
    def process_item(self, item, spider):
        with open('amazonbook.txt', 'a') as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
            f.write('\n')
        return item
