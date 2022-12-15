function Get-SumOfArrays  {
    param ($data)
    $result = New-Object System.Collections.ArrayList
    foreach ($arr in $data) {
        $res = $arr | Measure-Object -Sum
        $result += $res.Sum
    }
    return $result
}

function Get-ProblemOne {
    param ($data)
    $result = Get-SumOfArrays($data) | Measure-Object -Maximum
    return $result.Maximum
}

function Get-ProblemTwo {
    param ($data)
    $arr = Get-SumOfArrays($data) | Sort-Object -Descending
    $result = $arr[0..2] | Measure-Object -Sum
    return $result.Sum
}

$input = Get-Content "input.txt"
$int_arr = New-Object System.Collections.ArrayList
$container = New-Object System.Collections.ArrayList

foreach ($line in $input) {
    # Powershell does not treat empty strings as false.
    if ($line -ne "") {
        $int_arr += [int]$line
    }
    else {
        # If we don't include the ',' Powershell unpacks our array 🫠
        $container += , $int_arr
        # Could not get the Clear() method to actually work, so we just initialize a new array.
        $int_arr = New-Object System.Collections.ArrayList
    }
}

Write-Host "Problem one answer = $(Get-ProblemOne($container))"
Write-Host "Problem two answer = $(Get-ProblemTwo($container))"
