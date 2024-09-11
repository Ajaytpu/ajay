class Binary Search
{
int binary search (int arr[],int1,intr,intx)
{
if(r>=1)
{
int mid=1+(r-1)/2;
if (arr[mid]==X)
return mid;
if(arr[mid]>X)
return binary search [arr1,mid-1,x);
else 
return binary search [arr1,mid+1,r,x);
}
return -1;
}
public static void main (string args[])
{
Binary Search obj =new Binary Search();
int arr[]={2,4,6,8,10};
int n=arr.length;
int x=10;
int result=obj.binary search(arr,0,n-1,x);
if(result==1)
{
system.out.println("element is not found");
}
else
system.out.println("element is found at index:"+result);
