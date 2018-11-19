; ModuleID = 'code.c'
source_filename = "code.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: noinline nounwind optnone uwtable
define i32 @foo(i32, i32) #0 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  store i32 %1, i32* %4, align 4
  %5 = load i32, i32* %3, align 4
  %6 = load i32, i32* %4, align 4
  %7 = mul nsw i32 %5, %6
  ret i32 %7
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @bar(i32, i32) #0 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  store i32 %1, i32* %4, align 4
  %5 = load i32, i32* %3, align 4
  %6 = load i32, i32* %4, align 4
  %7 = sdiv i32 %5, %6
  ret i32 %7
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @far(i32, i32, i32) #0 {
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  store i32 %0, i32* %4, align 4
  store i32 %1, i32* %5, align 4
  store i32 %2, i32* %6, align 4
  store i32 3, i32* %7, align 4
  store i32 4, i32* %8, align 4
  store i32 5, i32* %9, align 4
  %10 = load i32, i32* %8, align 4
  %11 = load i32, i32* %8, align 4
  %12 = mul nsw i32 %10, %11
  %13 = load i32, i32* %9, align 4
  %14 = load i32, i32* %9, align 4
  %15 = mul nsw i32 %13, %14
  %16 = add nsw i32 %12, %15
  store i32 %16, i32* %7, align 4
  %17 = load i32, i32* %7, align 4
  %18 = load i32, i32* %7, align 4
  %19 = load i32, i32* %8, align 4
  %20 = sdiv i32 %19, 2
  %21 = call i32 @foo(i32 %18, i32 %20)
  %22 = load i32, i32* %8, align 4
  %23 = call i32 @bar(i32 %21, i32 %22)
  %24 = add nsw i32 %17, %23
  ret i32 %24
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @boo() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 12, i32* %1, align 4
  store i32 32, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  %4 = load i32, i32* %1, align 4
  %5 = add nsw i32 %3, %4
  %6 = sub nsw i32 0, %5
  %7 = load i32, i32* %2, align 4
  %8 = sub nsw i32 %7, 13
  %9 = sub nsw i32 0, %8
  %10 = add nsw i32 %6, %9
  store i32 %10, i32* %1, align 4
  store i32 2, i32* %2, align 4
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 32, i32* %2, align 4
  store i32 16, i32* %3, align 4
  %6 = load i32, i32* %2, align 4
  %7 = load i32, i32* %3, align 4
  %8 = mul nsw i32 %6, %7
  %9 = load i32, i32* %3, align 4
  %10 = load i32, i32* %4, align 4
  %11 = load i32, i32* %2, align 4
  %12 = sdiv i32 %10, %11
  %13 = call i32 @far(i32 %8, i32 %9, i32 %12)
  store i32 %13, i32* %4, align 4
  %14 = load i32, i32* %2, align 4
  %15 = mul nsw i32 %14, 2
  store i32 %15, i32* %3, align 4
  %16 = load i32, i32* %2, align 4
  %17 = load i32, i32* %3, align 4
  %18 = call i32 @foo(i32 %16, i32 %17)
  %19 = load i32, i32* %2, align 4
  %20 = load i32, i32* %3, align 4
  %21 = call i32 @foo(i32 %19, i32 %20)
  %22 = add nsw i32 %18, %21
  store i32 %22, i32* %5, align 4
  %23 = load i32, i32* %2, align 4
  %24 = load i32, i32* %2, align 4
  %25 = add nsw i32 %23, %24
  store i32 %25, i32* %5, align 4
  %26 = load i32, i32* %2, align 4
  %27 = load i32, i32* %3, align 4
  %28 = add nsw i32 %26, %27
  ret i32 %28
}

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"}
