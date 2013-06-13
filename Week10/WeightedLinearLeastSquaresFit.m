function [m,b,um,ub]=WeightedLinearLeastSquaresFit(x,y,w)
    m=((sum(w).*sum(w.*x.*y))-sum(w.*x).*sum(w.*y))/((sum(w).*sum(w.*x.*x))-(sum(w.*x)).^2);
    b=((sum(w.*x.*x).*sum(w.*y))-sum(x.*w).*sum(w.*x.*y))/((sum(w).*sum(w.*x.*x))-(sum(w.*x)).^2);
    if w==ones(size(w))
        u=y-(m.*x+b);
        n=len(x);
        um=((1/(n-2.)).*average(u^2)/(average(x.^2)-(average(x)).^2)).^.5;
        ub=((1/(n-2.)).*(average(u.^2).*average(x.^2))/(average(x.^2)-(average(x)).^2)).^.5;
    else
        um=(sum(w)/((sum(w).*sum(w.*x.*x))-sum(w.*x).^2)).^.5;
        ub=(sum(w.*x.*x)/((sum(w).*sum(w.*x.*x))-sum(w.*x).^2)).^.5;
    end
end