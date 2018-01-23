from lxml import etree
import requests


class XmlParser:
    urls_count = 0
    success_urls_count = 0
    failed_urls_count = 0
    failed_urls = {}

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def _clear_counters(self):
        self.urls_count = 0
        self.success_urls_count = 0
        self.failed_urls_count = 0

    def _create_report(self):
        failed_urls = self.failed_urls.items()

        with open(self.output_path, 'w+') as report:
            report.write('Parker report started.\n\n')
            report.write('Urls count: ' + str(self.urls_count) + '\n')
            report.write('Success URLs count: ' + str(self.success_urls_count) + '\n')
            report.write('Failed URLs count: ' + str(self.failed_urls_count) + '\n\n')

            if len(failed_urls) > 0:
                report.write('Failed URLs:\n')
                for url, error in failed_urls:
                    report.write(url + ' ' + error + '\n')

    def parse(self):
        xml = open(self.input_path, 'rb')
        content = xml.read()
        root = etree.XML(content)

        self._clear_counters()

        for node in root.getchildren():
            for elem in node.getchildren():
                if not elem.tag.endswith('loc'):
                    continue

                self.urls_count += 1
                url = elem.text or 'None'

                # TODO: Временный хардкод для тестов, попячить
                url = url.replace('http://novosibirsk.e2e4online.ru/shop/', 'https://e2e4.ru/nsk/')

                print("Testing URL " + url)

                try:
                    response = requests.get(url)

                    if response.status_code == 200:
                        self.success_urls_count += 1
                        continue

                    if response.status_code in [404, 500]:
                        self.failed_urls_count += 1
                        self.failed_urls[url] = response.status_code
                except:
                    self.failed_urls_count += 1
                    self.failed_urls[url] = 'Failed to connect'

        print('Urls count: ' + str(self.urls_count))
        print('Success urls count: ' + str(self.success_urls_count))
        print('Failed urls count: ' + str(self.failed_urls_count))

        self._create_report()

