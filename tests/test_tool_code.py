from nmap_scanner import NmapScanner

scanner = NmapScanner("127.0.0.1", "", "")

scanner.scan_and_save(filename='scan_result.csv')

results_as_csv = scanner.get_scan_results_as_csv()


print(results_as_csv)
