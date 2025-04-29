$done=$false
$wait_time=30

while (-not $done) {

$cores = Get-WmiObject -Query "SELECT * FROM Win32_PerfFormattedData_Counters_ProcessorInformation WHERE NOT Name LIKE '%_Total'"
foreach ($core in $cores) {
    $loadPercentage = $core.PercentProcessorTime
    $coreId = $core.Name.Replace(',', ' ')
    Write-Output "name=Custom Metrics|CPU|Core $coreId, value=$loadPercentage"
}    
	Start-Sleep -Seconds $wait_time
}