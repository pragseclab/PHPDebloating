<?php

/* privileges/initials_row.twig */
class __TwigTemplate_59e82b790234ac0e3009a03072f6fb355604f0773fecc5068152d5c148b7e03a extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<table id=\"initials_table\" cellspacing=\"5\">
    <tr>
        ";
        // line 3
        $context['_parent'] = $context;
        $context['_seq'] = twig_ensure_traversable((isset($context["array_initials"]) ? $context["array_initials"] : null));
        foreach ($context['_seq'] as $context["tmp_initial"] => $context["initial_was_found"]) {
            if ( !($context["tmp_initial"] === null)) {
                // line 4
                echo "            ";
                if ($context["initial_was_found"]) {
                    // line 5
                    echo "                <td>
                    <a class=\"ajax";
                    // line 7
                    echo (((array_key_exists("initial", $context) && ((isset($context["initial"]) ? $context["initial"] : null) === $context["tmp_initial"]))) ? (" active") : (""));
                    // line 8
                    echo "\" href=\"server_privileges.php";
                    // line 9
                    echo PhpMyAdmin\Url::getCommon(array("initial" => $context["tmp_initial"]));
                    echo "\">";
                    // line 10
                    echo $context["tmp_initial"];
                    // line 11
                    echo "</a>
                </td>
            ";
                } else {
                    // line 14
                    echo "                <td>";
                    echo $context["tmp_initial"];
                    echo "</td>
            ";
                }
                // line 16
                echo "        ";
            }
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_iterated'], $context['tmp_initial'], $context['initial_was_found'], $context['_parent'], $context['loop']);
        $context = array_intersect_key($context, $_parent) + $_parent;
        // line 17
        echo "        <td>
            <a href=\"server_privileges.php";
        // line 19
        echo PhpMyAdmin\Url::getCommon(array("showall" => 1));
        echo "\" class=\"nowrap\">
                ";
        // line 20
        echo _gettext("Show all");
        // line 21
        echo "            </a>
        </td>
    </tr>
</table>
";
    }

    public function getTemplateName()
    {
        return "privileges/initials_row.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  70 => 21,  68 => 20,  64 => 19,  61 => 17,  54 => 16,  48 => 14,  43 => 11,  41 => 10,  38 => 9,  36 => 8,  34 => 7,  31 => 5,  28 => 4,  23 => 3,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "privileges/initials_row.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/privileges/initials_row.twig");
    }
}
